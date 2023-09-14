import trimesh

# 读取 STL 文件
mesh = trimesh.load_mesh("data/ast-2M3-wl-张卫鹏-苏庭舒-46/ast-2M3-wl-张卫鹏-苏庭舒-46_0.stl")

# 创建场景
scene = trimesh.Scene(mesh)

# 设置相机参数
camera = scene.camera
camera.resolution = (800, 600)  # 设置分辨率
camera.transform = trimesh.transformations.euler_matrix(0, 0, 0)  # 设置相机的旋转和平移

# 渲染场景为图像
image = scene.save_image(visible=True)  # 设置 visible=True 以确保网格可见

# 保存为 PNG 图像文件
with open("out/imgs/stl_test.png", "wb") as f:
    f.write(image)
