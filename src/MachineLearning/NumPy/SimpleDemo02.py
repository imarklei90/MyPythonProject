# -*- encoding:utf-8 -*-

'''
    NumPy的简单示例
    两种基本的数据类型之矩阵
'''

from numpy import mat,matrix # mat 是 matrix的缩写

ss = mat([1,2,3])
print ss

mm = matrix([1,2,3])
print mm

# 访问矩阵中的单个元素
print mm[0,1]


pyList = [5,11,1605]
# 将Python列表转换成矩阵
print mat(pyList)

# 矩阵转置及相乘
print ss * mm.T

from numpy import shape

# 矩阵或者数组的维数
print shape(mm)

from numpy import multiply

# 矩阵对应元素相乘
print multiply(mm,ss)

# 矩阵排序
mm.sort()
print mm

# 矩阵的均值
print ss.mean()

#多维矩阵
jj = mat([[1,2,3],[3,3,3]])

print shape(jj)

# 取出第0行元素
print jj[0,:]

print jj[1,1:2]