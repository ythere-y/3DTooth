import open3d as o3d


file_name = (
    # "data/automate印模数据/automate印模数据1/AST-2M2-WL-严丽丽-曾德良-17/AST-2M2-WL-严丽丽-曾德良-17_0.pcd"
    # "data/automate印模数据/automate印模数据1/AST-2M2-WL-严丽丽-曾德良-17/Scans/Lower/MB Antagonist scan.pcd"
    "data/automate印模数据/automate印模数据1/AST-2M2-WL-严丽丽-曾德良-17/Scans/Lower/AntagonistScan.pcd"
)
# 读取 PCD 文件
point_cloud = o3d.io.read_point_cloud(file_name)

# 可视化点云
o3d.visualization.draw_geometries([point_cloud])
