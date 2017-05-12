# -*- encoding:utf-8 -*-
import urllib2
import cookielib

'''
    保存Cookie到变量
'''

#声明一个CookieJar对象实例来保存Cookie
cookie = cookielib.CookieJar()
#创建Cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#构建Opener
opener = urllib2.build_opener(handler)
response = opener.open("http://www.baidu.com")
for item in cookie:
    print "Name= " + item.name
    print "Value= " + item.value