# -*- encoding:utf-8 -*-
'''
    豆瓣Ajax请求
'''

import urllib
import urllib2

# https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=20
# https://movie.douban.com/j/chart/top_list?
url = "https://movie.douban.com/j/new_search_subjects?"
headers={"User-Agent": "Mozilla...."}

# 处理所有参数
formdata = {
    # 'type':'11',
    # 'interval_id':'100:90',
    # 'action':'',
    # 'start':'0',
    # 'limit':

    "sort":"T",
    "range":"0,10",
    "tags":"",
    "start":"0"
}


data = urllib.urlencode(formdata)

request = urllib2.Request(url, data = data, headers = headers)
response = urllib2.urlopen(request)

print response.read()