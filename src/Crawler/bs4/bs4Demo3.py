# -*- encoding:utf-8 -*-

'''
    信息组织与提取
    信息标记形式：
        XML： Internet上的信息交互与传递
        JSON：移动应用云端和节点的信息通信，无注释【主要用在程序对接口处理】
        YAML：各类系统的配置文件，有注释易读
        
    实例：
        提取HTML中所有的URL链接
        思路：
            1）搜素到所有<a>标签
            2）解析<a>标签格式，提取href后的链接内容
            
    bs4:
        <>.find_all(name, attrs, recursive, string, **kwargs)
        返回一个列表类型，存储查找的结果
        name：对标签名称的检索字符串
        attrs:对标签属性值的检索字符串，可标注属性检索
        recursive:是否对子孙全部检索，默认为True
        string:<>...</>中字符串区域的检索字符串
        
        注：
            <tag>.(..) 等价于<tag>.find_all(...)
            soup(...) 等价于soup.find_all(...)
            
        扩展方法：
            1） <>.find() 搜索且至返回一个结果，字符串类型，同.find_all()参数
            2） <>.find_parents() 在先辈节点中搜索，返回列表类型，同.find_all()参数
            3） <>.find_parent() 在先辈节点中返回一个结果，字符串类型，同.find()参数
            4） <>.find_next_siblings() 在后续平行节点中搜索，返回列表类型，同.find_all()参数
            5） <>.find_next_sibling() 在后续平行节点中搜索，返回一个结果，字符串类型，同.find()参数
            6） <>.find_previous_sibling() 在前序平行节点中搜索，返回列表类型，同.find_all()参数
            7） <>.find_previous_sibling() 在前序平行节点中搜索，返回一个结果，字符串类型，同.find()参数
'''

import requests
from bs4 import BeautifulSoup
import re

r = requests.get("http://www.python123.io/ws/demo.html")
demo = r.text

soup = BeautifulSoup(demo, 'html.parser')

for link in soup.find_all('a'):
    print link.get('href')

# bs4对HTML的搜索
print soup.find_all(['a','b'])

for tag in soup.find_all(True): # 参数为True，显示所有的标签名称
    print tag.name

for tag in soup.find_all(re.compile('b')): # 使用正则表达式找出b开头的标签
    print tag.name

print soup.find_all('p', 'course') # 检索标签的属性值
print soup.find_all(id = 'link1')
print soup.find_all(id = re.compile('link')) # 检索以link开头的标签

print soup.find_all('a')
print soup.find_all('a', recursive= False) # 只检索当前层次的节点

print soup.find_all(string = 'Basic Python')
print soup.find_all(string = re.compile('python'))