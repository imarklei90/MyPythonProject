#-*- encoding:utf-8 -*-

'''
    BeautifulSoap类对应的是HTML／XML文档的全部内容
    BeautifulSoap库解析器：
        1）bs4的html的解析器
        2）lxml的HTML解析器
        3）lxml的xml解析器
        4）html5lib的解析器
    BeautifulSoap类的五种基本类型：
        1）Tag：标签，最基本的信息组织单元<>、</>标明开头和结尾
        2）Name：标签名，<tag>.name
        3) Attributes:标签的属性，字典组织形式<tag>.attrs
        4) NavigableString:标签内非属性字符串<>...</>中的字符串，<tag>.string
        5) Comment:便签内字符串的注释部分，一种特殊的Comment类型
'''

import requests
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")

print (r.text)
# 指定HTML解析器
soup = BeautifulSoup(r.text, 'html.parser')
# 格式化HTML代码
print (soup.prettify())

print ('BeautifulSoap的属性操作')
# BS的属性操作
print (soup.a)
print (soup.a.parent.parent.name)

print (soup.a.attrs)
print (soup.a.attrs['href'])
print (type(soup.attrs))

print (soup.a.string)
print (soup.p.string)
print (type(soup.a.string))

# bs4的HTML格式化输出
print (soup.a.prettify())