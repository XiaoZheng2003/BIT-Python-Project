import os
import dic
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

'''以下是手动输入省份省会获取图像的代码
name=input("请输入省份及省会名，格式为“省份_省会”")
url='result/citybyYear/'+name+'.csv'#描述文件路径
try:
    data =np.loadtxt(url,dtype=str,delimiter=',')#读取csv文件为array格式，数据形式为str
except:
    print("输入错误")'''

os.makedirs("./result/images/",exist_ok=True)
#以下是自动生成所有城市图像的代码
for k,v in dic.dic.items():
    name=str(k)+'_'+str(v[0])
    url='result/citybyYear/'+name+'.csv'#描述文件路径
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
    if str(k)==str(v[0]):
        plt.title(str(v[0])+'平均高低温',fontproperties='SimHei',fontsize=20)
    else:
        plt.title(str(k)+str(v[0])+'平均高低温',fontproperties='SimHei',fontsize=20)
    plt.xlabel('年份/年(注：2022年数据截至8月）',fontproperties='SimHei',fontsize=10)
    plt.ylabel('温度/℃',fontproperties='SimHei',fontsize=10)
    x_major_locator=MultipleLocator(1)
    #把x轴的刻度间隔设置为1，并存在变量里
    
    ax=plt.gca()
    #ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    #把x轴的主刻度设置为1的倍数
   
    for x,y in zip(years1,ave_max1):
        plt.text(x-0.5,y-0.7,'  '+str(y)+'℃',fontdict={'fontsize':7})
    #在图像中加数据标识
    for x,y in zip(years1,ave_min1):
        plt.text(x-0.5,y+0.7,'  '+str(y)+'℃',fontdict={'fontsize':7})
    #在图像中加数据标识
    
    plt.plot(years1,ave_max1,'ro-',years1,ave_min1,'bo-')
    #去掉下行注释可以保存图像
    plt.savefig('result/images/'+name+'平均高低温',dpi=600)#保存PNG图像，文件名为”省份_省会平均高低温“
    #plt.show()

    #清空绘图以免第二张图像保留第一张内容
    plt.clf() # 清图。



    #生成极端高温低温图像
    if str(k)==str(v[0]):
        plt.title(str(k)+'极端高低温',fontproperties='SimHei',fontsize=20)
    else:
        plt.title(str(k)+str(v[0])+'极端高低温',fontproperties='SimHei',fontsize=20)
    plt.xlabel('年份/年(注：2022年数据截至8月）',fontproperties='SimHei',fontsize=10)
    plt.ylabel('温度/℃',fontproperties='SimHei',fontsize=10)
    x_major_locator=MultipleLocator(1)
    #把x轴的刻度间隔设置为1，并存在变量里
    
    ax=plt.gca()
    #ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    #把x轴的主刻度设置为1的倍数
    
    for x,y in zip(years1,t_max1):
        plt.text(x-0.3,y-2,'  '+str(y)+'℃',fontdict={'fontsize':7})
    #在图像中加数据标识
    for x,y in zip(years1,t_min1):
        plt.text(x-0.3,y+2,'  '+str(y)+'℃',fontdict={'fontsize':7})
    #在图像中加数据标识
    
    plt.plot(years1,t_max1,'ro-',years1,t_min1,'bo-')
    #plt.show()
    #去掉下行注释可以保存图像
    plt.savefig('result/images/'+name+'极端高低温',dpi=600)#保存PNG图像，文件名为”省份_省会极端高低温“

    #清空绘图以免第二张图像保留第一张内容
    plt.clf() # 清图。