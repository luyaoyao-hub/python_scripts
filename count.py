# ---用于计算一个文件夹里有多少个文件---

import os


def count_files_in_directory(directory_path):
    try:
        # 获取目录中的文件列表
        files_list = os.listdir(directory_path)

        # 使用 len() 函数获取文件数量
        file_count = len(files_list)

        print(f"文件夹 {directory_path} 中包含 {file_count} 个文件。")
    except Exception as e:
        print(f"Error: {e}")


# 指定要计数文件的目录路径
directory_to_count = 'F:\\hairball'


# 调用函数计数文件数量
count_files_in_directory(directory_to_count)
