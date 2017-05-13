# -*- encoding:utf-8 -*-

'''
    向百度提交搜索关键词，百度的搜索接口是：http://www.baidu.com/s？wd=keyword
'''
import requests
try:
    kv = {'wd':'Python'}
    r = requests.get('http://www.baidu.com/s',params=kv)
    print r.request.url
    r.raise_for_status()
    print len(r.text)
except:
    print '解析失败'
