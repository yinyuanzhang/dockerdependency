# @Time    : 2020/8/20 16:10
# @Author  : yinyuanzhang@nudt.edu.cn

import os
from numpy import *
import re
import csv
import pandas as pd





def gci(filepath):
    # 遍历filepath下所有文件，包括子目录
    global i,z
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            gci(fi_d)
        else:
            print(i)
            print(filepath)
            print(fi_d)
            from_repo = filepath.split('\\')[-1]
            image[i][0] = from_repo
            print(image[i][0])
            source_image.add(image[i][0])
            #read2(filepath, fi_d)
            #       print(image[i][1])
            print('\n')

    return image





# 解析大量的dockerfile文件，数据清洗后，获取 source和target images
i = 0
m = 0
n = 0
image = [[1 for col in range(2)] for row in range(140000)]


# 递归遍历/root目录下所有文件

j = 0
z = 0


print(type(image))
source_image = set()
gci('A:\dockerfiles-1.0.0\data')
print(len(source_image))