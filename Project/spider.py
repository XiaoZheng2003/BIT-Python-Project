from bs4 import BeautifulSoup
from xpinyin import Pinyin
import requests
import time
import dic

def getHTMLText(url:str):
    """
    该函数负责根据传入的url，爬取响应的网页界面，并返回网页的html代码。

    若爬取时出现错误，函数将会返回False.

    @参数 url：爬取网页的url，包括协议头（如http://），字符串类型
    """
    try:
        kv={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63'}
        r=requests.get(url,timeout=30,headers=kv)
        time.sleep(2)                               #防止请求过快，爬虫受限
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return False

def getProvincefromCity(dic:dict,city:str)->str:
    """
    该函数负责接受一个城市名，返回它所对应的省。

    @参数 dic：省市字典，字典类型。
    @参数 city：输入城市的名字，字符串类型。
    """
    for key,value in dic.items() :
        if city in value :
            return key
        
def getCityList(dic:dict)->list:
    """
    该函数负责导出一个城市列表。

    @参数 dic：省市字典，字典类型。
    """
    ls=[]
    for value in dic.values():
        for city in value:
            ls.append(city)
    return ls
    
def completeUrl(city:str,date:str)->str:
    """
    该函数负责对于网址的合成，返回为一个字符串，为该省份历史天气的url。

    示例：https://lishi.tianqi.com/beijing/202207.html

    @参数 city：城市名称，如北京，字符串类型。
    @参数 date：要查询的年月，如2022年7月为202207，字符串类型。
    """
    if city!='重庆':
        pinyin=Pinyin().get_pinyin(city,'')
    else:
        pinyin="chongqing"
    return "https://lishi.tianqi.com/"+pinyin+'/'+date

def statistic(info:list)->list:
    """
    根据各月份的天气信息，统计出一年的平均高温、平均低温、极端高温、极端低温信息，返回四个数值。

    传入为二维列表，分别代表1-12月的信息。

    @参数 info：每个月的四个数值，列表类型，列表为字符串类型。
    """
    t_max=-100
    max_sum=0
    min_sum=0
    t_min=100
    t_avemax=0
    t_avemin=0
    for i in info:
        max_sum+=eval(i[0])
        min_sum+=eval(i[1])
        if eval(i[2])>t_max:
            t_max=eval(i[2])
        if eval(i[3])<t_min:
            t_min=eval(i[3])
    t_avemax=max_sum/len(info)
    t_avemin=min_sum/len(info)
    return round(t_avemax,1),round(t_avemin,1),t_max,t_min


def analyse(text:str):
    """
    分析爬取的网页，并返回为一个列表，包括平均高温、平均低温、极端高温、极端低温四个信息。

    列表为字符串类型。

    @参数 text：网页的内容，字符串类型。
    """
    soup=BeautifulSoup(text,"html.parser")
    ls=soup.find_all(class_="tian_twoa")
    if not ls:
        return False
    ans=[]
    for item in ls:
        ans.append(item.text[:-1])
    return ans[0:4]

def annualWeather(city:str,year:str)->list:
    """
    分析该年的气温情况，返回为平均高温、平均低温、极端高温、极端低温，四个数值。
    
    输入错误返回为False。

    @参数 city：代分析城市的名称，字符串类型。
    @参数 year：分析的年份，字符串类型。
    """
    ls=[]
    nowyear=time.strftime("%Y",time.localtime())
    nowmonth=time.strftime("%m",time.localtime())
    if nowmonth[0]=='0':
        nowmonth=nowmonth[1:]
    for i in range(1,(eval(nowmonth)+1) if year==nowyear else 13):
        url=completeUrl(city,year+"{:0>2d}".format(i))
        text=getHTMLText(url)
        cnt=0
        while not text:
            print("{}天气获取错误！".format(city))
            cnt+=1
            reportError(text,cnt)
            text=getHTMLText(url)
        t=analyse(text)
        while not t:
            print("{}天气获取错误！".format(city))
            cnt+=1
            reportError(text,cnt)
            text=getHTMLText(url)
            t=analyse(text)
        ls.append(t)
    return statistic(ls)

def reportError(text,num:int):
    """
    该函数为报告错误函数，将会为当前时间生成一个日志文件，保存当时的网页内容

    @参数 text：报错时的网页内容，字符串类型，或为False。
    """
    if not text:
        return
    if num>10:
        print('错误次数达到上限！程序自动退出！')
        quit()
    f=open('error_{}.txt'.format(time.strftime("%Y%m%d%H%M%S",time.localtime())),"w",encoding='utf-8')
    f.write(text)
    f.close()

def getYear()->str:
    """
    从输入获取需要爬取的年份信息，并检查其合法性。返回值为获取的年份，字符串类型。
    """
    nowyear=time.strftime("%Y",time.localtime())
    year=input("请输入你要获取的年份信息（范围2011-{}）：".format(nowyear))
    while not year.isdigit() or eval(year)>eval(nowyear) or eval(year)<2011:
        print("输入错误！请重新输入")
        year=input("请输入你要获取的年份信息（范围2011-{}）：".format(nowyear))
    return year

def main():
    ls=getCityList(dic.dic)
    year=getYear()
    f=open("result-{}年.csv".format(year),"w",encoding='utf-8')
    f.write("省份,城市,平均高温,平均低温,极端高温,极端低温\n")
    for city in ls:
        res=annualWeather(city,year)
        f.write("{},{},{},{},{},{}\n".format(getProvincefromCity(dic.dic,city),city,res[0],res[1],res[2],res[3]))
        print("{},{},{},{},{},{}".format(getProvincefromCity(dic.dic,city),city,res[0],res[1],res[2],res[3]))


if __name__ == '__main__':
    main()