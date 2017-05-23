# -*- encoding:utf-8 -*-
'''
    NumPy的简单示例
    两种基本的数据类型之数组
'''

from numpy import *

mm = array((1,2,3))

pp = array((1,2,3))

print mm + pp

print mm * 2

print mm **2

print pp[2]

dd = array([[1,2,3],[1,2,3]])
print dd[1][2]

print dd[1,2] # 矩阵方式访问多维数组

# 两个数组相乘
aa = array([1,2,3])
bb = array([0.3,0.2,0.1])
print aa * bb