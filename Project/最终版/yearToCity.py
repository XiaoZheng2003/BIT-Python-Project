"""
将各年份的天气数据统计汇总成各城市近十年的天气数据。
"""

import os

filename_ls = os.listdir('result/citybyYear/')
f = []
os.makedirs("./result/year/", exist_ok=True)
for file in filename_ls:
    f.append(open("result/citybyYear/"+file, encoding='gbk'))
for i in range(2010, 2023):
    for j in range(len(f)):
        ls = f[j].readline().replace('\n', '').split(',')
        if i == 2010:
            continue
        if j == 0:
            fw = open("result/year/{}年天气情况.csv".format(i), "w", encoding="gbk")
            fw.write("省份,城市,平均高温,平均低温,极端高温,极端低温\n")
        else:
            fw = open("result/year/{}年天气情况.csv".format(i), "a", encoding="gbk")
        f_ls = filename_ls[j].replace('.csv', '').split('_')
        fw.write(','.join(f_ls)+','+','.join(ls[1:])+'\n')
