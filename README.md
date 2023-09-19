# Tooth Project

## 数据预览

共75个项目，每个项目



## 工作记录

将stl文件转为pcd文件

stl文件转为png文件可视化(`src/save_stl_into_png.py`)

pointNet训练

目前3D模型只能用点云图片来处理


将dcm文件转为点云文件
    首先将dcm文件使用Windows软件转为stl文件(done)
    然后将stl文件转为pcd文件(done)(`src/convert_stl_into_pcd.py`)

## PointNet Model

[PointNet Colab](https://colab.research.google.com/drive/17mcQr0uJd_yyPCB_xFas_Rx__QIcloD6#scrollTo=CnrEK4Um5Yro)

模型数据
Total params: 7370062 (28.11 MB)
Trainable params: 7356110 (28.06 MB)
Non-trainable params: 13952 (54.50 KB)

## Train Data

Num train point clouds: 2955
Num train point cloud labels: 2955
Num val point clouds: 739
Num val point cloud labels: 739

