# -*- encoding:utf-8 -*-

import re

#将正则表达式编译成Pattern对象
pattern = re.compile(r'hello')

#使用re.match匹配文本
result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo zzz')
result3 = re.match(pattern, 'helo aaa')
result4 = re.match(pattern, 'hello zzz')

if result1:
    # 获得分组信息
    print result1.group()
else:
    print '1匹配失败'

if result2:
    print result2.group()
else:
    print '2匹配失败'

if result3:
    # 获得分组信息
    print result3.group()
else:
    print '3匹配失败'

if result4:
    print result4.group()
else:
    print '4匹配失败'
