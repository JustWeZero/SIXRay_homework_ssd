# config.py
import os.path

# gets home dir cross platform
# HOME = os.path.expanduser("~")
# modify by lzj at 2019-12-9 修改项目路径
# HOME = r'D:\Python_Project\ssd.pytorch-master\battery_dataset_unbalance\train'
HOME = r'/home/g203-server3/ssd.pytorch-master/battery_dataset_unbalance/train'

# for making bounding boxes pretty
COLORS = ((255, 0, 0, 128), (0, 255, 0, 128), (0, 0, 255, 128),
          (0, 255, 255, 128), (255, 0, 255, 128), (255, 255, 0, 128))

MEANS = (104, 117, 123)

# SSD300 CONFIGS
# voc = {
#     'num_classes': 21,
#     'lr_steps': (80000, 100000, 120000),
#     # 'max_iter': 120000,
#     'max_iter': 5000,
#     'feature_maps': [38, 19, 10, 5, 3, 1],
#     'min_dim': 300,
#     'steps': [8, 16, 32, 64, 100, 300],
#     'min_sizes': [30, 60, 111, 162, 213, 264],
#     'max_sizes': [60, 111, 162, 213, 264, 315],
#     'aspect_ratios': [[2], [2, 3], [2, 3], [2, 3], [2], [2]],
#     'variance': [0.1, 0.2],
#     'clip': True,
#     'name': 'VOC',
# }

# modify by lzj 20191209 自己的数据集参数
SIXRay = {
    'num_classes': 3,
    'lr_steps': (80000, 100000, 120000),
    # 'lr_steps': (80, 100, 120),
    'max_iter': 120000,
    # 'max_iter': 2000,
    'feature_maps': [38, 19, 10, 5, 3, 1],
    'min_dim': 300,
    'steps': [8, 16, 32, 64, 100, 300],
    'min_sizes': [30, 60, 111, 162, 213, 264],
    'max_sizes': [60, 111, 162, 213, 264, 315],
    'aspect_ratios': [[2], [2, 3], [2, 3], [2, 3], [2], [2]],
    'variance': [0.1, 0.2],
    'clip': True,
    'name': 'SIXRay',
}

coco = {
    'num_classes': 201,
    'lr_steps': (280000, 360000, 400000),
    'max_iter': 400000,
    'feature_maps': [38, 19, 10, 5, 3, 1],
    'min_dim': 300,
    'steps': [8, 16, 32, 64, 100, 300],
    'min_sizes': [21, 45, 99, 153, 207, 261],
    'max_sizes': [45, 99, 153, 207, 261, 315],
    'aspect_ratios': [[2], [2, 3], [2, 3], [2, 3], [2], [2]],
    'variance': [0.1, 0.2],
    'clip': True,
    'name': 'COCO',
}
