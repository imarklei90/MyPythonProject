import urllib2

request = urllib2.Request("http://blog.csdn.net/imail2016")

try:
    urllib2.urlopen(request)
except urllib2.HTTPError,e:
    print e.code
except urllib2.URLError3,e:
    if hasattr(e,"reason"): # 对异常的属性进行判断
        print e.reason
else:
    print 'OK'