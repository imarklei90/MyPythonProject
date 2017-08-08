#-*- encoding:utf-8 -*-
'''
    自定义Hander和Opener
'''

import urllib2


# 构建http handler
# http_handler = urllib2.HTTPHandler()

# debug模式
http_handler = urllib2.HTTPHandler(debuglevel=1)

# 构建自定义opener
opener = urllib2.build_opener(http_handler)
request = urllib2.Request("http://www.baidu.com")

# 通过open方法发送请求
response = opener.open(request)
print response.read()