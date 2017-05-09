#-*- encoding=UTF-8 -*-

# Test a Simple Crawler

__author__ = 'leiguan'

import urllib2

response = urllib2.urlopen("http://www.dlworld.cn/YeJieDongTai/3860.html")
print response.read()