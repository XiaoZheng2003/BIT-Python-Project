"""
将各市每月的天气数据汇总成一年。
"""
import os
import pandas as pd

def init(file:str)->pd.DataFrame:
    """
    读取csv文件，并返回DataFrame类型。

    @参数 file：csv文件名，字符串格式。
    """
    df=pd.read_csv(file,encoding='gbk')
    df=df.drop_duplicates()
    return df
    
def statistic(info:list)->list:
    """
    根据各月份的天气信息，统计出一年的平均高温、平均低温、极端高温、极端低温信息，返回四个数值。

    传入为二维列表，分别代表各月的信息。

    @参数 info：每个月的四个数值，列表类型，列表为数字类型。
    """
    month_day=[31,28,31,30,31,30,31,31,30,31,30,31]
    t_max=-100                                  #极端高温
    max_sum=0                                   #平均高温之和
    min_sum=0                                   #平均低温之和
    t_min=100                                   #极端低温
    t_avemax=0                                  #一年内平均高温
    t_avemin=0                                  #一年的平均低温
    day=0                                       #一年的天数
    for t,i in enumerate(info):
        max_sum+=i[0]*month_day[t]        #求和
        min_sum+=i[1]*month_day[t]
        day+=month_day[t]
        if i[2]>t_max:
            t_max=i[2]
        if i[3]<t_min:
            t_min=i[3]
    t_avemax=max_sum/day                        #求平均值
    t_avemin=min_sum/day
    return round(t_avemax,1),round(t_avemin,1),t_max,t_min

def pick(df:pd.DataFrame,year:str)->list:
    """
    从pandas的数据中选取该年份的数据，并将该年份的所有月份数据按照时间、平均高温、平均低温、极端高温、极端低温的顺序返回。返回为二维列表类型。

    @参数 df：存放该城市所有月份的数据。为pandas的DataFrame类型。
    @参数 year：代表所需年份的数据。
    """
    df=df[df['时间'].str.contains(year)]
    order=['月平均最高气温','月平均最低气温','月最高气温','月最低气温']
    return df[order].values.tolist()

def main():
    file_ls=os.listdir('result/citybyMonth/')
    os.makedirs("./result/citybyYear/",exist_ok=True)
    for file in file_ls:
        f=open("result/citybyYear/"+file,"w",encoding='gbk')
        f.write("年份,平均高温,平均低温,极端高温,极端低温\n")
        df=init("result/citybyMonth/"+file)
        for year in range(2011,2023):
            ls=pick(df,str(year))
            print(file,year)
            ans=statistic(ls)
            f.write("{},{},{},{},{}\n".format(year,ans[0],ans[1],ans[2],ans[3]))

if __name__ == '__main__':
    main()



