# -*- encoding:utf-8 -*-

import urllib2
import cookielib

'''
    从文件中获取Cookie并访问
'''

#创建Cookie实例对象
cookie = cookielib.MozillaCookieJar()

#从文件中读取Cookie数据到变量
cookie.load('CookieSave.txt',ignore_discard= True, ignore_expires= True)

#创建Request
request = urllib2.Request("http://www.baidu.com")

#创建Opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(request)
print response.read()