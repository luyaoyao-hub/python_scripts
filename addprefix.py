# ---在指定的文件前面加前缀---

import os


def add_prefix(directory, prefix):
    for filename in os.listdir(directory):
        # 之前我不明白为什么要路径拼接，不拼接的话，就是一个固定的文件名称，就不能批量处理文件了
        if os.path.isfile(os.path.join(directory, filename)):
            new_name = f"{prefix}{filename}"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))


# 指定目录和前缀
directory_path = r'F:\txt\slit'
prefix = 'slit_'

add_prefix(directory_path, prefix)

