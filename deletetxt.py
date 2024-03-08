# 这个脚本用于删除指定名字的json文件，有些json文件不需要了，我要把它删除，需要删除的json的文件有1000多个。需要用脚本来删除
import os
from os import listdir

# 指定包含要删除文件名的文本文件路径
file_list_Path = 'F:\\end.txt'

# 读取文件名列表
with open(file_list_Path, 'r') as file:
    file_to_delete = file.read().splitlines()

    # print(file_to_delete)

# 指定要删除文件的目录
directory_path = 'F:\\txt'

# 遍历文件名列表并删除文件
for filename in file_to_delete:
    # 构建完整的文件路径
    file_path = os.path.join(directory_path, filename)

    try:
        os.remove(file_path)
        print(f"{filename}删除成功")
    except OSError as e:
        print(f"Error:{filename}删除失败 - {e}")
