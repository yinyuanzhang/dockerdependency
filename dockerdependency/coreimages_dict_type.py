# @Time    : 2020/8/8 10:59
# @Author  : yinyuanzhang@nudt.edu.cn

import os
from numpy import *
import re
import csv
import pandas as pd




dataframe = pd.read_csv('A:\\pythonproject2\\key-value.csv')      # 读取core image 信息
imagepairs = dataframe.values.tolist()
print(imagepairs)
print(type(imagepairs))



k = list()
v = list()
for i in range(len(imagepairs)):
    k.append(imagepairs[i][0])
    v.append(imagepairs[i][1])


d = dict(zip(k,v))

print(d)