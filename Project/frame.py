from bs4 import BeautifulSoup
from xpinyin import Pinyin
import requests
import time

def getHTMLText(url:str):
    """
    该函数负责根据传入的url，爬取响应的网页界面，并返回网页的html代码。

    若爬取时出现错误，函数将会返回False.

    @参数 url：爬取网页的url，包括协议头（如http://），字符串类型
    """
    try:
        kv={'user-agent':'Mozilla/5.0'}
        r=requests.get(url,timeout=30,headers=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return False

def Inthelist(list,n):
    for i in list:
        if(i == n) :
            return True
        else:return False

def getCityName(dic,n):
    """
    该函数负责从json中解析出省市信息，返回为一个列表，包括各市的信息（不包含“市”）。

    @参数 dic：省市字典的文件名，字典类型。
    @参数 n:输入城市的名字，字符串类型。
    """
    for key,value in dic.items() :
        if n==value :
            return key


def completeUrl(city:str,date:str)->str:
    """
    该函数负责对于网址的合成，返回为一个字符串，为该省份历史天气的url。

    示例：https://lishi.tianqi.com/beijing/202207.html

    @参数 city：城市名称，如北京，字符串类型。
    @参数 date：要查询的年月，如2022年7月为202207，字符串类型。
    """
    return "https://lishi.tianqi.com/"+Pinyin().get_pinyin(city,'')+'/'+date

def statistic(info:list)->list:
    """
    根据各月份的天气信息，统计出一年的平均高温、平均低温、极端高温、极端低温信息，返回四个数值。

    传入为二维列表，分别代表1-12月的信息。

    @参数 info：每个月的四个数值，列表类型，列表为字符串类型。
    """

    ...

def analyse(text:str)->list:
    """
    分析爬取的网页，并返回为一个列表，包括平均高温、平均低温、极端高温、极端低温四个信息。

    列表为字符串类型。

    @参数 text：网页的内容，字符串类型。
    """
    soup=BeautifulSoup(text,"html.parser")
    ls=soup.find_all(class_="tian_twoa")
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
    ans=[]
    nowyear=time.strftime("%Y",time.localtime())
    nowmonth=time.strftime("%m",time.localtime())
    for i in range(1,(eval(nowmonth)+1) if year==nowyear else 13):
        url=completeUrl(city,year+"{:0>2d}".format(i))
        text=getHTMLText(url)
        ans.append(analyse(text))
    return statistic(ans)

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
    ls=getCityList()
    year=getYear()
    f=open("result-{}年.csv".format(year),"w",encoding='utf-8')
    f.write("省份,城市,平均高温,平均低温,极端高温,极端低温\n")
    for city in ls:
        res=annualWeather(city,year)
        f.write("{},{},{},{},{},{}\n".format(getProvincefromCity(city),city,res[0],res[1],res[2],res[3]))


if __name__ == '__main__':
    main()