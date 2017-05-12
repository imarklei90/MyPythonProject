# -*- encoding:utf-8 -*-

# 匹配对象和组（放置在（）中的子模式，组的序号取决于它左侧的括号数，组0就是整个模式）
import re

pattern = r'www\.(.*)\..{3}'
m = re.match(pattern, 'www.python.org')

# group获取给定子模式（组）的匹配项
print m.group(1)

# start end返回给定组的匹配项的开始和结束位置（和分片一样，不包括组的结束位置）
print m.start(1)
print m.end(1)

# span返回一个组的开始和结束位置
print m.span(1)