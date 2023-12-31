"""
根据每年的数据绘制成天气数据热力图。
"""

import os
import math
import pandas as pd
from pyecharts.charts import Map
from pyecharts import options as opts

ls = ['平均高温', '平均低温', '极端高温', '极端低温']
for year in range(2011, 2023):
    # 读取excel中数据
    df = pd.read_csv("result/year/{}年天气情况.csv".format(year),
                     encoding='gbk',
                     index_col=None,
                     header=0,
                     converters={'省份': str},
                     usecols=['省份', '平均高温', '平均低温', '极端高温', '极端低温'])
    for row in range(4):
        # 地图热力图
        # 将pandas.DataFrame格式的数据，每一行转为元组tuple，所有数据以列表list输出
        data = df[['省份', ls[row]]].apply(
            lambda x: tuple(x), axis=1).values.tolist()
        temp = df[ls[row]].values  # 将该列数据保存
        _max = math.ceil(max(temp))  # 将最大值上取整
        _min = math.floor(min(temp))  # 将最小值下取整
        map_ = Map()
        map_.add("省份{}".format(ls[row]), data, maptype="china", zoom=1)  # 设置图例
        map_.set_global_opts(
            title_opts=opts.TitleOpts(title="{}年{}".format(year, ls[row]),  # 设置标题
                                      pos_right="center",
                                      pos_top="5%"),
            visualmap_opts=opts.VisualMapOpts(max_=_max,
                                              min_=_min,
                                              # range_color=['green','yellow','red']
                                              # 此处可自定义颜色
                                              ),
        )
        os.makedirs("./result/html/", exist_ok=True)  # 创建文件夹
        map_.render("result/html/{}年{}.html".format(year, ls[row]))  # 保存热力图
