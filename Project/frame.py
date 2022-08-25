from bs4 import BeautifulSoup
import requests

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

def getCityName(file:str)->list:
    """
    该函数负责从json中解析出省市信息，返回为一个列表，包括各市的信息（不包含“市”）。

    @参数 file：省市json的文件名，字符串类型。
    """

    ...

def completeUrl(city:str,date:str)->str:
    """
    该函数负责对于网址的合成，返回为一个字符串，为该省份历史天气的url。

    示例：https://lishi.tianqi.com/beijing/202207.html

    @参数 city：城市拼音，如北京为beijing，字符串类型。
    @参数 date：要查询的年月，如2022年7月为202207，字符串类型。
    """

    ...

def statistic(info:list)->list:
    """
    根据各月份的天气信息，统计出一年的平均高温、平均低温、极端高温、极端低温信息，返回四个数值。

    @参数 info：每个月的四个数值，列表类型。
    """

    ...

def analyse(text:str)->list:
    """
    分析爬取的网页，并返回为一个列表，包括平均高温、平均低温、极端高温、极端低温四个信息。

    @参数 text：网页的内容，字符串类型。
    """

    ...