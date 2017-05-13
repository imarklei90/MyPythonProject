# -*- encoding:utf-8 -*-
'''
    爬虫通用处理框架
'''

import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status() # 如果返回的状态码不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding # 使得返回内容的解码是正确的
        return r.text
    except:
        return '产生异常'

if __name__ == "__main__":
    url = "http://www.baidu.com"
    print getHTMLText(url)

