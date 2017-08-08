# -*- encoding:utf-8 -*-
'''
    爬虫代理服务器
'''

import urllib2

proxy_switch = True
# 构建一个Handler处理器
http_proxy_handler = urllib2.ProxyHandler({"http":"183.30.197.181:9797"})

# 没有代理的处理器对象
null_proxy_handler = urllib2.ProxyHandler({})

if proxy_switch:
    opener = urllib2.build_opener(http_proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)

# 构建了一个全局的opener,之后所有的请求都通过urlopen()的方式发送
urllib2.install_opener(opener)
request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
print response.read()