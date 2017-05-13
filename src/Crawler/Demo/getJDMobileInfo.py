#-*- encoding:utf-8 -*-

'''
    获取京东手机信息
'''
import requests

def getJDInfo(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        print r.status_code
        r.encoding = r.apparent_encoding
        print r.text[:1000]
    except:
        print '获取信息失败'

if __name__ == '__main__':
    getJDInfo('https://item.jd.com/3979765.html')