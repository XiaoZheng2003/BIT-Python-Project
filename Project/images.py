import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

#由于我还不会导入别的文件中的字典所以直接copy过来了，如果有人可以做到直接导入的话麻烦优化，非常之感谢
dic = {
    '北京': ['北京'],
    '上海': ['上海'],
    '天津': ['天津'],
    '重庆': ['重庆'],
    '黑龙江': ['哈尔滨'],
    '吉林': ['长春'],
    '辽宁': ['沈阳'],
    '内蒙古': ['呼和浩特'],
    '河北': ['石家庄'],
    '新疆': ['乌鲁木齐'],
    '甘肃': ['兰州'],
    '青海': ['西宁'],
    '陕西': ['西安'],
    '宁夏': ['银川'],
    '河南': ['郑州'],
    '山东': ['济南'],
    '山西': ['太原'],
    '安徽': ['合肥'],
    '湖北': ['武汉'],
    '湖南': ['长沙'],
    '江苏': ['南京'],
    '四川': ['成都'],
    '贵州': ['贵阳'],
    '云南': ['昆明'],
    '广西': ['南宁'],
    '西藏': ['拉萨'],
    '浙江': ['杭州'],
    '江西': ['南昌'],
    '广东': ['广州'],
    '福建': ['福州'],
    '台湾': ['台北'],
    '海南': ['海口'],
    # '香港': ['香港'],
    # '澳门': ['澳门'],
    # 香港、澳门历史天气数据不全
}

'''以下是手动输入省份省会获取图像的代码
name=input("请输入省份及省会名，格式为“省份_省会”")
url='../result/city/'+name+'.csv'#描述文件路径
try:
    data =np.loadtxt(url,dtype=str,delimiter=',')#读取csv文件为array格式，数据形式为str
except:
    print("输入错误")'''


#以下是自动生成所有城市图像的代码
for k,v in dic.items():
    name=str(k)+'_'+str(v[0])
    url='../result/city/'+name+'.csv'#描述文件路径
    data =np.loadtxt(url,dtype=str,delimiter=',')#读取csv文件为array格式，数据形式为str

    #每一列数据分别读取
    years=data[1:,0]
    ave_max=data[1:,1]
    ave_min=data[1:,2]
    t_max=data[1:,3]
    t_min=data[1:,4]
    #转换为int和float
    years1=np.array(list(map(int, years)))
    ave_max1 = np.array(list(map(float, ave_max)))
    ave_min1 = np.array(list(map(float, ave_min)))
    t_max1 = np.array(list(map(float, t_max)))
    t_min1 = np.array(list(map(float, t_min)))



    #生成平均高温低温图像
    plt.title(name+'平均高低温',fontproperties='SimHei',fontsize=20)
    plt.xlabel('年份/年',fontproperties='SimHei',fontsize=10)
    plt.ylabel('温度/℃',fontproperties='SimHei',fontsize=10)
    x_major_locator=MultipleLocator(1)
    #把x轴的刻度间隔设置为1，并存在变量里
    
    ax=plt.gca()
    #ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    #把x轴的主刻度设置为1的倍数
   
    for x,y in zip(years1,ave_max1):
        plt.text(x,y,'%.1f' % y+'℃',fontdict={'fontsize':7})
    #在图像中加数据标识
    for x,y in zip(years1,ave_min1):
        plt.text(x,y,'%.1f' % y+'℃',fontdict={'fontsize':7})
    #在图像中加数据标识
    plt.plot(years1,ave_max1,'ro-',years1,ave_min1,'bo-')
    #去掉下行注释可以保存图像
    plt.savefig('../result/images/'+name+'平均高低温',dpi=600)#保存PNG图像，文件名为”省份_省会平均高低温“
    #plt.show()

    #清空绘图以免第二张图像保留第一张内容
    plt.clf() # 清图。



    #生成极端高温低温图像
    plt.title(name+'极端高低温',fontproperties='SimHei',fontsize=20)
    plt.xlabel('年份/年',fontproperties='SimHei',fontsize=10)
    plt.ylabel('温度/℃',fontproperties='SimHei',fontsize=10)
    x_major_locator=MultipleLocator(1)
    #把x轴的刻度间隔设置为1，并存在变量里
    
    ax=plt.gca()
    #ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    #把x轴的主刻度设置为1的倍数
    
    for x,y in zip(years1,t_max1):
        plt.text(x,y,'%.1f' % y+'℃',fontdict={'fontsize':7})
    #在图像中加数据标识
    for x,y in zip(years1,t_min1):
        plt.text(x,y,'%.1f' % y+'℃',fontdict={'fontsize':7})
    #在图像中加数据标识
    plt.plot(years1,t_max1,'ro-',years1,t_min1,'bo-')
    #plt.show()
    #去掉下行注释可以保存图像
    plt.savefig('../result/images/'+name+'极端高低温',dpi=600)#保存PNG图像，文件名为”省份_省会极端高低温“

    #清空绘图以免第二张图像保留第一张内容
    plt.clf() # 清图。