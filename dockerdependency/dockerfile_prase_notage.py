import os
from numpy import *
import re
import csv
import pandas as pd




# 遍历文件夹下所有的文件
def gci(filepath):
    global i
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            gci(fi_d)
        else:      #  直到fi_d 是文件，就可以获取到dockerfile文件
            print(i)
            print(filepath)
            print(fi_d)
            from_repo = filepath.split('\\')[-1]
            image[i][0] = from_repo
            print(image[i][0])
            read(filepath, fi_d)
            print('\n')
    return image


# 解析dockerfile文件 进行数据清洗
def read(filepath,fi_d):
    global i,m,n                                   #m,n 是用来确定多from指令的数量
    file_inside = open(fi_d, encoding='gb18030', errors='ignore')
    k = 0
    l = 0

    for line in file_inside:
        if ("FROM" in line) and (line.split("FROM")[0].strip() == "") and (line.split("FROM")[-1].strip() != ","):   #定位到FROM指令，但排除#注释下的FROM指令，根据经验排除 FROM 后 跟着 ","
            if(k == 0):    # k是用来判断是否是该文件第一次读取到“FROM”指令
                image_before = line.split("FROM")[-1].split(":")[0].strip()          # 忽视image的版本号差异
                if((" as " in image_before) or (" AS " in image_before)):            # 提取出 as 或 AS 写法中的指令参数
                    image_before = image_before.split(" as ")[0].strip()
                    image_before = image_before.split(" AS ")[0].strip()
                if ((len(image_before) > 0) and ("$" not in image_before)):
                    image[i][1] = image_before.split("/")[-1]
                    if(image[i][1] != image[i][0] and len(image[i][1]) != 0):     # 排除自我依赖

                        print(image[i][1])
                        k = k + 1
                        i = i + 1
                       # limit = limit + 1

            elif(k == 1):
                image_before2 = line.split("FROM")[-1].split(":")[0].strip()
                if((" as " in image_before2) or (" AS " in image_before2)):            # 提取出 as 或 AS 写法中的指令参数
                    image_before2 = image_before2.split(" as ")[0].strip()
                    image_before2 = image_before2.split(" AS ")[0].strip()
                if ((len(image_before2) > 0) and ("$" not in image_before2)):
                    image[i][1] = image_before2.split("/")[-1]
                    if (image[i][1] != image[i - 1][1]) and (image[i][1] != image[i - 1][0]):  # 针对多from指令 选取前一个未曾出现的  and  排除自我依赖

                        image[i][0] = image[i - 1][0]
                        print(image[i][1])
                        if (len(image[i][1]) != 0):
                            k = k + 1
                            i = i + 1
                      #  limit = limit + 1

                            m = m + 1
                        print("------------------------------------------------" + str(m))

            else:
                image_before3 = line.split("FROM")[-1].split(":")[0].strip()
                if((" as " in image_before3) or (" AS " in image_before3)):            # 提取出 as 或 AS 写法中的指令参数
                    image_before3 = image_before3.split(" as ")[0].strip()
                    image_before3 = image_before3.split(" AS ")[0].strip()
                if ((len(image_before3) > 0) and ("$" not in image_before3)):
                    image[i][1] = image_before3.split("/")[-1]
                    if (image[i][1] != image[i - 1][1]) and (image[i][1] != image[i - 2][1]) and (image[i][1] != image[i-1][0]):  # 针对多from指令 选取前一个未曾出现的  and  排除自我依赖

                        image[i][0] = image[i - 1][0]
                        print(image[i][1])
                        if (len(image[i][1]) != 0):
                            i = i + 1
                       # limit = limit + 1

                        n = n + 1
                        print("++++++++++++++++++++++++++++++++++++++++++++" + str(n))

                        break






# 解析大量的dockerfile文件，数据清洗后，获取 source和target images
i = 0
m = 0
n = 0
image = [[1 for col in range(2)] for row in range(130000)]


gci('A:\dockerfiles-1.0.0\data')
for m in range(i,130000):
    del image[i]

column = ['source', 'target']             #offical_tage 用来判断
test = pd.DataFrame(columns=column, data=image)
test.to_csv('A://pythonproject2//' + 'dockerfile_prase_notage.csv',index=False)