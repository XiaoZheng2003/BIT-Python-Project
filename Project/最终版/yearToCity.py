"""
将各年份的天气数据统计汇总成各城市近十年的天气数据。
"""

import os

filename_ls = os.listdir('result/citybyYear/')  # 获取文件列表
f = []  # 存放文件句柄列表
os.makedirs("./result/year/", exist_ok=True)  # 创建文件夹
for file in filename_ls:
    f.append(open("result/citybyYear/"+file, encoding='gbk'))  # 将文件全部打开
for i in range(2010, 2023):
    for j in range(len(f)):  # 遍历文件列表
        ls = f[j].readline().replace('\n', '').split(',')  # 将数据转换成列表
        if i == 2010:  # 跳过第一行表头
            continue
        if j == 0:
            fw = open("result/year/{}年天气情况.csv".format(i),
                      "w", encoding="gbk")  # 第一次打开覆盖写
            fw.write("省份,城市,平均高温,平均低温,极端高温,极端低温\n")  # 写入表头
        else:
            fw = open("result/year/{}年天气情况.csv".format(i),
                      "a", encoding="gbk")  # 后续打开追加写
        f_ls = filename_ls[j].replace('.csv', '').split('_')
        fw.write(','.join(f_ls)+','+','.join(ls[1:])+'\n')  # 写入数据
