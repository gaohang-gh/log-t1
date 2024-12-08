import pandas as pd
# 使用原始字符串处理路径
input_file = r"C:\Users\Lenovo\.dataset\bgl\BGL.log"  # 原始文件路径
output_file = r"C:\Users\Lenovo\.dataset\bgl\BGL_10000.log"  # 保存路径

m = (int)(1e6)

# 读取原始文件并截取前1万行
with open(input_file, 'r', encoding='utf-8') as infile:
    lines = infile.readlines()[:m]  # 读取前1万行

# 保存为新的文件
with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.writelines(lines)  # 将前1万行写入新的文件

