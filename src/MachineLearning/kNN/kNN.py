# -*- encoding:utf-8 -*-

'''
    kNN算法实现对电影进行分类
'''

from numpy import *
import operator


# 创建数据集
def createDataSet():
    group = array([[1.0,1.1], [1.0,1.0], [0,0], [0,0.1]])
    labels = ['A','A','B','B']
    return group, labels


# 实现kNN算法（使用kNN算法将每组数据划分到某个类中）
def classify0(inX, dataSet, labels, k): # 用于分类的输入向量inX,输入的训练样本集,标签向量lables,选择最近邻居的数目
    dataSetSize = dataSet.shape[0]
    # 距离计算（使用欧式距离公式）
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distance = sqDistances ** 0.5

    # 选择距离最小的个点
    sortedDistIndicies = distance.argsort()
    classCount = {}
    for i in range(k):
        votelabel = labels[sortedDistIndicies[i]]
        classCount[votelabel] = classCount.get(votelabel, 0) + 1

    # 排序
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

if __name__ == '__main__':
    group, labels = createDataSet()
    print group
    print labels

    print classify0([0,0], group, labels, 3)
