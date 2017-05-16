#-*- encoding=UTF-8 -*-

import urllib2

request = urllib2.Request("http://www.baidaau.com")
try:
    response = urllib2.urlopen(request)
except urllib2.URLError,e: # 加入了URLError
    print e.reason
print response.read() # response 对象的read(),可以返回获取到的网页内容