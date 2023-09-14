import open3d as o3d
import matplotlib.pyplot as plt

# 加载点云文件
point_cloud = o3d.io.read_point_cloud("out/test.pcd")

# 可视化点云
o3d.visualization.draw_geometries([point_cloud])

# 截取当前窗口的图像
image = o3d.visualization.draw_geometries_with_animation_callback([point_cloud])

# 保存可视化结果为图像文件
# o3d.visualization.draw_geometries_to_file("out/imgs/test.png", [point_cloud])

# 保存图像文件
plt.imsave("out/imgs/test.png", image)

# 保存点云文件
# o3d.io.write_point_cloud("path/to/your/output_pointcloud.pcd", point_cloud)
