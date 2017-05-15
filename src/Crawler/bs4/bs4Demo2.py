# -*- encoding:utf-8 -*-

'''
    bs4库的遍历：
        1）标签树的下行遍历
            .contents:子节点的列表，将<tag>所有儿子节点存入列表
            .children:子节点的迭代类型，与.contents类似，用于循环遍历儿子节点
            .descendants:子孙节点的迭代类型，包含所有子孙节点，用于循环遍历
            for child in soup.body.children
        2) 标签树的上行遍历
            .parent 节点的父亲标签
            .parents 节点先辈标签的迭代类型，用于循环遍历先辈节点
        3) 标签树的平行遍历
            .next_sibling:返回按照HTML文本顺序的下一个平行节点标签
            .previous_sibling:返回按照HTML文本顺序的上一个平行节点标签
            .next_siblings:迭代类型，返回按照HTML文本顺序的后续所有平行节点标签
            .previous_siblings:迭代类型，返回按照HTML文本顺序的前续所有平行节点标签
            条件：平行遍历发生在同一个父节点下的各节点间
'''

import requests

from bs4 import BeautifulSoup

r = requests.get('http://www.python123.io/ws/demo.html')
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')

print soup.head
print soup.head.contents

print soup.body.contents
print len(soup.body.contents)
print soup.body.contents[1]

print soup.title.parent

# 标签树的上行遍历
for parent in soup.a.parent:
    if parent is None:
        print parent
    else:
        print parent.name

# 便签的平行遍历
print soup.a.next_sibling
print soup.a.next_sibling.next_sibling
print soup.a.previous_sibling