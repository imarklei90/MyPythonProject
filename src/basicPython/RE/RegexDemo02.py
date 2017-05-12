# -*- encoding:utf-8 -*-
import re

# 根据包含正则表达式的字符串创建模式对象
pattern = re.compile(r'py')

# 在字符串的开始处匹配模式（在指定字符串的开头匹配正则表达式）
if re.match(pattern, 'python'):
    print 'Found It'
else:
    print '在字符串的开始出未找到字符串'

# 在字符串中寻找模式（在指定字符串中寻找第一个匹配正则表达式的子字符串）
if re.search(pattern, 'aaPythonpython'):
    print 'Found python'
else:
    print '在字符串中没有找到匹配的子字符串'

# 使用模式匹配项分割字符串
some_data = 'alpha.beta.....gamma.delta'
print re.split('[.]+', some_data)
# 最多分割两次
print re.split('[.]+', some_data, maxsplit= 2)

print re.split('o(o)', 'FoooooBar')

# findall以列表的形式返回给定模式的所有匹配项
pattern = '[a-zA-Z]+'
content = '"Hell... aaa --- *** are you ok?" he said. sounds good'
print re.findall(pattern, content)

# 查找标点符号
pattern = r'[.?\-.]+'
print re.findall(pattern, content)

# sub使用给定的替换内容将匹配模式的子字符串（最左端并且非重叠的子字符串）替换掉
pattern = '{name}'
content = 'Dear {name}...{name}---{name}'
print re.sub(pattern, 'Mr HAHA', content)

# escape 对字符串中所有可能被解释为正则运算符的字符进行转义
print re.escape('www.python.org')
print re.escape('Hello Python And Regex')
