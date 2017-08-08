# -*- encoding:utf-8 -*-
'''
    POST请求
'''

import urllib
import urllib2

# http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}

form_data = {
    "i": "java",
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"1502096575948",
    "sign":"22056f7e382a6cfbc7d69907660e32fd",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_ENTER",
    "typoResult":"true"
}

data = urllib.urlencode(form_data)

request = urllib2.Request(url, data=data, headers=headers)
response = urllib2.urlopen(request)
print response.read()