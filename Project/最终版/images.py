"""
根据各城市近十年的数据绘制折线图。
"""

import os
import dic
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


def manual():
    """
    以下是手动输入省份省会获取图像的代码。
    """
    while True:
        name = input(
            "请输入省份及省会名，格式为“省份_省会”，例如“福建_福州”。\n" +
            "注：直辖市请输入城市名，格式为“直辖市_直辖市”，例如“重庆_重庆”。\n")  # 输入提示信息
        url = 'result/citybyYear/'+name+'.csv'  # 描述文件路径
        try:
            # 读取csv文件为array格式，数据形式为str
            data = np.loadtxt(url, dtype=str, delimiter=',')
            k = name.split('_')[0]
            v = name.split('_')[1]
            process(data, k, v)  # 绘制图像
            break
        except:
            print("输入错误！请重新输入")


def auto():
    """
    以下是自动生成所有城市图像的代码。
    """
    for k, v in dic.dic.items():  # 遍历字典
        name = str(k)+'_'+str(v[0])  # 文件名
        url = 'result/citybyYear/'+name+'.csv'  # 描述文件路径
        # 读取csv文件为array格式，数据形式为str
        data = np.loadtxt(url, dtype=str, delimiter=',')
        process(data, k, v[0])  # 绘制图像


def process(data, k, v):
    """
    程序进行绘图操作的代码。
    """
    # 设置图像文件名
    name = str(k)+'_'+str(v)
    # 每一列数据分别读取
    years = data[1:, 0]
    ave_max = data[1:, 1]
    ave_min = data[1:, 2]
    t_max = data[1:, 3]
    t_min = data[1:, 4]
    # 转换为int和float
    years1 = np.array(list(map(int, years)))
    ave_max1 = np.array(list(map(float, ave_max)))
    ave_min1 = np.array(list(map(float, ave_min)))
    t_max1 = np.array(list(map(float, t_max)))
    t_min1 = np.array(list(map(float, t_min)))

    # 生成平均高温低温图像
    if str(k) == str(v):
        plt.title(str(v)+'平均高低温', fontproperties='SimHei',
                  fontsize=20)  # 直辖市标题
    else:
        plt.title(str(k)+str(v)+'平均高低温',
                  fontproperties='SimHei', fontsize=20)  # 省份省会标题
    plt.xlabel(
        '年份/年(注：2022年数据截至8月）', fontproperties='SimHei', fontsize=10)  # x轴
    plt.ylabel('温度/℃', fontproperties='SimHei', fontsize=10)  # y轴

    '''
    将x轴的单位长度设置为1
    '''
    x_major_locator = MultipleLocator(1)
    # 把x轴的刻度间隔设置为1，并存在变量里

    ax = plt.gca()
    # ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    # 把x轴的主刻度设置为1的倍数

    for x, y in zip(years1, ave_max1):
        plt.text(x-0.5, y-0.7, '  '+str(y)+'℃', fontdict={'fontsize': 7})
    # 在图像中加数据标识

    for x, y in zip(years1, ave_min1):
        plt.text(x-0.5, y+0.7, '  '+str(y)+'℃', fontdict={'fontsize': 7})
    # 在图像中加数据标识

    # 绘制图像
    plt.plot(years1, ave_max1, 'ro-', years1, ave_min1, 'bo-')
    # 保存PNG图像，文件名为“省份_省会平均高低温”
    plt.savefig('result/images/'+name+'平均高低温', dpi=600)
    # plt.show()

    # 清空绘图以免第二张图像保留第一张内容
    plt.clf()  # 清图

    # 生成极端高温低温图像
    if str(k) == str(v):
        plt.title(str(k)+'极端高低温', fontproperties='SimHei',
                  fontsize=20)  # 直辖市标题
    else:
        plt.title(str(k)+str(v)+'极端高低温',
                  fontproperties='SimHei', fontsize=20)  # 省份省会标题
    plt.xlabel(
        '年份/年(注：2022年数据截至8月）', fontproperties='SimHei', fontsize=10)  # x轴
    plt.ylabel('温度/℃', fontproperties='SimHei', fontsize=10)  # y轴

    '''
    将x轴的单位长度设置为1
    '''
    x_major_locator = MultipleLocator(1)
    # 把x轴的刻度间隔设置为1，并存在变量里

    ax = plt.gca()
    # ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    # 把x轴的主刻度设置为1的倍数

    for x, y in zip(years1, t_max1):
        plt.text(x-0.3, y-2, '  '+str(y)+'℃', fontdict={'fontsize': 7})
    # 在图像中加数据标识
    for x, y in zip(years1, t_min1):
        plt.text(x-0.3, y+2, '  '+str(y)+'℃', fontdict={'fontsize': 7})
    # 在图像中加数据标识

    # 绘制图像
    plt.plot(years1, t_max1, 'ro-', years1, t_min1, 'bo-')
    # plt.show()
    # 保存PNG图像，文件名为”省份_省会极端高低温“
    plt.savefig('result/images/'+name+'极端高低温', dpi=600)

    # 清空绘图以免第二张图像保留第一张内容
    plt.clf()  # 清图


def main():
    os.makedirs("./result/images/", exist_ok=True)  # 创建文件夹
    manual()  # 手动输入省份省会获取图像
    # auto()  # 自动生成所有城市图像


if __name__ == '__main__':
    main()
