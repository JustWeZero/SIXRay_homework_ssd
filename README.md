# X光图像检测的数据不平衡问题
------

## 问题综述

题目给出了安检的X光图片，目的是检测出给定的X光图片里是否有带电芯的充电宝或不带电芯的充电宝，若有需要得到充电宝的像素坐标位置。训练一个目标检测模型，使用这个目标检测模型检测出测试集中每张图片中的危险品（例如输入模型一张测试图片，最终输出这张图片中所有危险品的类别以及位置坐标）。

此外，给定的数据集中存在数据不平衡问题，带电芯充电宝只有500张图片而不带电芯的充电宝有5000张图片，这样势必会导致训练的时候出现问题，比如将所有的疑似点都认成不带电芯的充电宝就可以得到很好的正确率。

## 问题分析

根据分析，题目是一个目标检测问题，当前的目标检测问题主流解决方法通常使用深度学习处理。目前大致可分为two-stage和one-stage两种。

Two-stage，代表算法Fast-RCNN，Faster-RCNN等，主要原理是通过RPN产生一系列稀疏的候选框，对候选框进行分类或回归。准确率较高。One-stage，代表算法YOLO和SSD，主要原理是在图片的不同位置使用不同尺度和长宽比密集抽样，然后利用CNN提取特征直接分类或者回归。速度较快。**根据考虑后本组选择目前速度较快准确率较高的SSD方法作为处理方法。**

对于数据不平衡问题，通常的解决方法有增加训练集，上采样或下采样，利用已知样本生成新样本增加训练集，通过改变损失函数减少不平衡问题影响。由于增加数据集这一选项不可取，下采样会减少训练集而上采样不能很好的解决问题，直接生成新样本效果未必理想且新生成的图像标注比较耗时。本组折中了上采样和生成新样本，**使用数据增强的方式增添训练集。**

## 模型介绍

### 结构

Single Shot MultiBox Detector（SSD）是一种One-stage目标检测算法，它使用VGG16作为其backbone，具体结构如下图：

![](https://github.com/Helixuan/SIXRay_Homework_ssd/blob/master/SSD_constructure.png)

它在VGG-16的基础上进行修改，把之前的两个全连接层FC6，FC7改成$1\times1$和$3\times3$的卷积层，并且删掉dropout和全连接层FC8后添加了一系列卷积层训练。在多个feature map上做分类，最后使用NMS得到最后的结果。

### 与其他算法的显著区别

SSD的与YOLO等算法的不同点在于：

1. 不同于YOLO在卷积层后接全连接层，相当于只使用了最高层的feature map，SSD采用金字塔结构，利用了多个卷积层上的feature map，在多个feature map上做分类和回归。通过这种方式使用感受野小的feature map检测小目标，使用感受野大的feature map检测更大目标。
2. 借鉴了Faster-RCNN的anchor思想，使用了Prior Box，即一些目标的预选框，后续通过回归得到真实的目标位置，设定具体如下：

|             | Min_size | Max_size |
| :---------: | :------: | :------: |
| **Conv4_3** |    30    |    60    |
|   **Fc7**   |    60    |   111    |
| **Conv6_2** |   111    |   162    |
| **Conv7_2** |   162    |   213    |
| **Conv8_2** |   213    |   264    |
| **Conv9_2** |   264    |   315    |

### 损失函数

SSD设计了一种针对目标检测的损失函数multibox
$$
L(x,c,l,g)=\frac{1}{N}\left(L_{conf}(x,c)+\alpha L_{loc}(x,l,g)\right)
$$
损失函数是confidence loss(conf)和localization loss(loc)的加权相加。其中loc定义为预测框与ground truth的L1损失，conf采用softMax 损失函数。

此外，可以使用Focal loss损失函数，该函数主要解决了负样本太多的问题，也就是说可以进一步解决样本不均衡的问题，由于时间有限还进行尝试。

### 数据增强

本组使用数据增强解决数据不平衡问题。主要采取的手段有

- 直接使用原始的图像（即不进行变换）
- 采样一个patch，保证与GT之间最小的IoU为：0.1，0.3，0.5，0.7 或 0.9
- 完全随机的采样一个patch
- 采样的patch占原始图像大小比例在[0.1,1]之间
- 采样的patch的长宽比在[0.5,2]之间
- 当 Ground truth box中心恰好在采样的patch中时，保留整个GT box
- 最后每个patch被resize到固定大小，并且以0.5的概率随机的水平翻转

## 结果发表

训练

最后结果：mAP : 0.8308 , core_AP : 0.7735 , careless_AP : 0.8880。

![](https://github.com/Helixuan/SIXRay_Homework_ssd/blob/master/test_result.png)



