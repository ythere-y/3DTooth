import open3d as o3d

from utils.files import get_all_stl_files
from tqdm import tqdm


def single_test():
    # 读取STL文件
    mesh = o3d.io.read_triangle_mesh(
        # "data/ast-2M3-wl-张卫鹏-苏庭舒-46/ast-2M3-wl-张卫鹏-苏庭舒-46_0.stl"
        "data/automate印模数据/automate印模数据1/AST-2M2-WL-严丽丽-曾德良-17/Scans/Lower/AntagonistScan.stl"
    )

    # 转换为点云
    point_cloud = mesh.sample_points_poisson_disk(10000)  # 通过采样生成点云，可调整点的数量

    # 保存点云文件
    o3d.io.write_point_cloud("out/test.pcd", point_cloud)


def batch_convert():
    files = get_all_stl_files()
    for f in tqdm(files):
        # 读取STL文件
        mesh = o3d.io.read_triangle_mesh(f)

        # 转换为点云
        point_cloud = mesh.sample_points_poisson_disk(10000)

        # 保存点云文件
        o3d.io.write_point_cloud(f.replace(".stl", ".pcd"), point_cloud)


if __name__ == "__main__":
    single_test()
    batch_convert()
