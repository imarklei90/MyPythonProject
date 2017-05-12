# -*- encoding:utf-8 -*-
import urllib2
import cookielib

'''
保存Cookie到文件中
'''

#设置保存Cookie的文件
fileName = "CookieSave.txt"

#声明一个CookieJar对象保存Cookie信息，之后写入文件
cookie = cookielib.MozillaCookieJar(fileName)

#创建Cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)

#构建Opener
opener = urllib2.build_opener(handler)

#创建request
response = opener.open("http://www.baidu.com")

#保存Cookie到文件
cookie.save(ignore_discard=True,ignore_expires=True) # 即使Cookie将被丢弃，也将它保存下来，如果Cookie已经存在，则覆盖

