# -*- encoding:utf-8 -*-
'''
    Cookie
'''

import urllib
import urllib2
import cookielib

# 创建一个CookieJar的值，用来保存Cookie的值
cookie = cookielib.CookieJar()

# 构建处理器对象，用来处理Cookie
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(cookie_handler)
opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36")]

url = "http://www.renren.com/PLogin.do"

data = {"email":"*", "password":"*"}

data = urllib.urlencode(data)
request = urllib2.Request(url, data=data)
response = opener.open(request)

print response.read()