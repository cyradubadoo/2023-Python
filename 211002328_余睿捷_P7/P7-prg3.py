#查找工作目录下所有Python文件（.py文件），然后将所有Python文件复制到新建文件夹python_code下，
# 最后压缩该文件夹，压缩后的文件命名为python_code.zip。

import os
import shutil
import zipfile

# 定义工作目录和目标文件夹:当前目录
work_dir = "."
target_dir = "./python_code"

# 如果目标文件夹不存在，就创建它
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

#复制
for file in os.listdir(work_dir):
    file_path = os.path.join(work_dir, file)    #获取完整的文件路径
    if file_path.endswith(".py"):
        shutil.copy(file_path, target_dir)

#压缩
zip_file = zipfile.ZipFile("./python_code.zip", "w")


for file in os.listdir(target_dir):
    file_path = os.path.join(target_dir, file)
    zip_file.write(file_path, compress_type=zipfile.ZIP_DEFLATED) # 将Python文件添加到压缩文件中，并指定压缩方式为ZIP_DEFLATED

zip_file.close()