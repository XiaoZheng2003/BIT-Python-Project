"""
负责天气网站数据的爬取，返回为各个城市各个月份的天气数据。
注：该程序从http://www.tianqihoubao.com/ 获取天气信息
"""

from bs4 import BeautifulSoup
from xpinyin import Pinyin
import requests
import time
import dic
import os


def getHTMLText(url: str):
    """
    该函数负责根据传入的url，爬取响应的网页界面，并返回网页的html代码。

    若爬取时出现错误，函数将会返回False.

    @参数 url：爬取网页的url，包括协议头（如http://），字符串类型
    """
    MAX_RETRY = 3  # 最大出错次数
    retry = 0  # 当前出错次数
    while retry < MAX_RETRY:
        try:
            kv = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102\
            Safari/537.36 Edg/104.0.1293.63'}  # 添加user-agent，防止被网站拒绝访问
            r = requests.get(url, timeout=30, headers=kv)
            time.sleep(10)  # 防止请求过快，爬虫受限
            r.raise_for_status()  # 若网站返回非200的错误代码，则报错
            return r.text
        except:
            retry += 1  # 错误次数加一
            time.sleep(10)  # 出错后，程序暂停一段时间
            print("{} 出错！第{}次重试".format(url, retry))
    return False


def getProvincefromCity(dic: dict, city: str) -> str:
    """
    该函数负责接受一个城市名，返回它所对应的省。

    @参数 dic：省市字典，字典类型。
    @参数 city：输入城市的名字，字符串类型。
    """
    for key, value in dic.items():
        if city in value:
            return key


def getCityList(dic: dict) -> list:
    """
    该函数负责返回一个城市列表。

    @参数 dic：省市字典，字典类型。
    """
    ls = []
    for value in dic.values():
        for city in value:
            ls.append(city)
    return ls


def completeUrl(city: str, month: str) -> str:
    """
    该函数负责对于网址的合成，返回为一个字符串，为该省份历史天气的url。

    示例：http://www.tianqihoubao.com/lishi/xianggang/1.html

    @参数 city：城市名称，如北京，字符串类型。
    @参数 date：要查询的月份，如7月为7，字符串类型。
    """
    if city == '重庆':  # 重庆进行特殊处理，否则返回zhongqing
        pinyin = 'chongqing'
    elif city == '福州':  # 福州进行特殊处理
        pinyin = 'fujianfuzhou'
    else:  # 其他情况程序自动转换拼音
        pinyin = Pinyin().get_pinyin(city, '')
    return "http://www.tianqihoubao.com/lishi/"+pinyin+'/'+month+'.html'


def analyse(text: str) -> list:
    """
    分析爬取的网页，并返回为一个二维列表，包括时间、平均高温、平均低温、极端高温、极端低温四个信息。

    列表为字符串类型。

    @参数 text：网页的内容，字符串类型。
    """
    soup = BeautifulSoup(text, "html.parser")  # 解析网页内容
    ls = []
    tr = soup.find(class_="b").find_all('tr')  # 解析表格
    for i in tr[1:]:  # 忽略表头
        td = i.find_all('td')
        tls = []
        for t in range(5):  # 遍历数据
            if t:
                tls.append(td[t].get_text().strip().replace(
                    ' ', '')[:-1])  # 保留年月
            else:
                tls.append(td[t].get_text().strip().replace(
                    ' ', ''))  # 舍去温度末尾的℃，便于数据处理
        ls.append(tls)  # 加入列表中
    return ls


def reportError(url: str, text, num: int):
    """
    该函数为报告错误函数，将会以当前时间为文件名，生成一个日志文件，保存当时的网页内容。

    @参数 url：报错时的网页链接，字符串类型。
    @参数 text：报错时的网页内容，字符串类型，或为False，代表未能获取网页内容。
    @参数 num：产生错误的次数，整数类型。
    """
    os.makedirs("./log/", exist_ok=True)  # 新建log文件夹
    f = open('./log/error_{}.log'.format(time.strftime("%Y%m%d%H%M%S",
             time.localtime())), "w", encoding='utf-8')
    print("产生错误的网址为：{}".format(url))
    f.write("Error Url:{}\n".format(url))
    maxError = 5  # 最大错误次数
    if num >= maxError:  # 超过最大错误次数，则退出程序
        print('错误次数达到上限！程序自动退出！')
        exit()
    if not text:  # 如果未获取到网页信息，则不写入log文件
        return
    f.write(text)  # 写入网页信息
    f.close()  # 保存日志文件


def main():
    os.makedirs("./result/citybyMonth/", exist_ok=True)
    ls = getCityList(dic.dic)  # 获取城市列表
    for city in ls:  # 遍历城市
        f = open("./result/citybyMonth/{}_{}.csv".format(
            getProvincefromCity(dic.dic, city), city), "w", encoding='gbk')  # 创建数据文件
        f.write("时间,月最高气温,月最低气温,月平均最高气温,月平均最低气温\n")
        for month in range(1, 13):  # 从1至12月分别获取数据
            url = completeUrl(city, str(month))  # 补充网址
            text = getHTMLText(url)  # 获取网页信息
            ls = analyse(text)  # 分析文本
            for line in ls:
                f.write(','.join(line)+'\n')  # 写入数据
            print(city+str(month)+"月保存成功！")  # 程序输出成功信息提示用户


if __name__ == '__main__':
    main()
