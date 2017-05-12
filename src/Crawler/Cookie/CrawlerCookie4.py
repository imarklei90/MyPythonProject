# -*- encoding:utf-8 -*-

import urllib
import urllib2
import cookielib

'''
    利用Cookie模拟登录
'''

#声明Cookie对象，并保存到文件
fileName = 'save'
cookie = cookielib.MozillaCookieJar(fileName)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postData = urllib.urlencode({
    'username':'Admin',
    'password':'123'
})

#模拟登录的URL
loginURL = "http://www.baidu.com/login"

#模拟登录，保存Cookie到变量
result = opener.open(loginURL, postData)

#保存Cookie到文件
cookie.save(ignore_discard=True, ignore_expires= True)

#利用Cookie请求访问另一个网址
anotherURL = "http://www.baidu.com/xxx"

result = opener.open(anotherURL)

print result.read()