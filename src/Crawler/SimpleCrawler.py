#-*- encoding=UTF-8 -*-

# Test a Simple Crawler

__author__ = 'leiguan'

import urllib2

response = urllib2.urlopen("https://zhuanlan.zhihu.com/p/26799224?group_id=845278956881055744")
print response.read()