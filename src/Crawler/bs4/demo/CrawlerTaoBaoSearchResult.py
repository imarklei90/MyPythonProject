# -*- encoding:utf-8 -*-

'''
    定向获取淘宝搜索商品价格数据
'''

import requests
import re


def getTaoBaoSearchInfo(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parseTaoBaoSearchInfo(infoLists, html):
    try:
        title = re.findall(r'\"title\"\:\"\.*?"', html)
        price = re.findall(r'\"price\"\:\"[\d\.]*\"', html)
        for i in range(len(title)):
            title = eval(title[i].split(':')[1])
            price = eval(price[i].split(':')[1])
            print "------" + title + price
            infoLists.append([title, price])
    except:
        print ""


def printTaoBaoSearchInfo(infoLists):
    tplt = '{:4}\t{:16}\t{:8}'
    print tplt.format("序号","名称","价格")
    count = 0

    for i in infoLists:
        count = count + 1
        print "infoLists:" + i
        print tplt.format(count, i[0],i[1])


def main():
    searchData = '笔记本电脑'
    depth = 3
    start_url = "https://s.taobao.com/search?q=" + searchData
    infoLists = []

    for i in range(depth):
        try:
            url = start_url + '&s=' + str(48 * i)
            html = getTaoBaoSearchInfo(url)
            parseTaoBaoSearchInfo(infoLists, html)
        except:
            continue

    printTaoBaoSearchInfo(infoLists)

main()