import os
import glob


def get_all_stl_files(directory: str = "data"):
    stl_files = []
    # 遍历根目录及其子目录下的所有文件
    for root, directories, files in os.walk(directory):
        for file in files:
            if file.endswith(".stl"):
                # 获取文件路径
                file_path = os.path.join(root, file)
                # 在这里执行你想要的操作，比如读取、处理或者打印文件路径
                stl_files.append(file_path)

    return stl_files
