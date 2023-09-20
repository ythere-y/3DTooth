# Tooth Project

## 数据预览

共75个项目，每个项目



## 工作记录

将stl文件转为pcd文件

stl文件转为png文件可视化(`src/save_stl_into_png.py`)

pointNet训练

目前3D模型只能用点云图片来处理


将dcm文件转为点云文件
    
    首先将dcm文件使用Windows软件转为stl文件
    然后将stl文件转为pcd文件

## PointNet训练

### 训练数据

4045张有标注的3D图片（飞机）


![1](data/PartAnnotation/02691156/expert_verified/seg_img/1a04e3eab45ca15dd86060f189eb133.png)
![2](data/PartAnnotation/02691156/expert_verified/seg_img/1a29042e20ab6f005e9e2656aff7dd5b.png)


每张图片转为1024个点组成的点云图片。标注了4个部分：body, wing, tail, engine。

![1](out/imgs/point_cloud_0.png)
![2](out/imgs/point_cloud_300.png)

### 模型参数


模型数据
Total params: 7370062 (28.11 MB)
Trainable params: 7356110 (28.06 MB)
Non-trainable params: 13952 (54.50 KB)

### 训练参数

`epoch = 60`

### 训练结果

loss 曲线
![loss](out/train_info/loss.png)

accuracy 曲线
![accuracy](out/train_info/accuracy.png)
## PointNet Model

[PointNet Colab](https://colab.research.google.com/drive/17mcQr0uJd_yyPCB_xFas_Rx__QIcloD6#scrollTo=CnrEK4Um5Yro)


