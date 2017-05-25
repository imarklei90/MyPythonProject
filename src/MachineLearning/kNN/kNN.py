# -*- encoding:utf-8 -*-

'''
    kNN算法实现:
        对电影进行分类
        改进约会网站的效果
'''

from numpy import *
import operator
import matplotlib.pyplot as plt


# 创建数据集
def createDataSet():
    group = array([[1.0,1.1], [1.0,1.0], [0,0], [0,0.1]])
    labels = ['A','A','B','B']
    return group, labels


# 实现kNN算法（使用kNN算法将每组数据划分到某个类中）
def classify0(inX, dataSet, labels, k):  # 用于分类的输入向量inX,输入的训练样本集,标签向量lables,选择最近邻居的数目
    # 训练集的维度
    dataSetSize = dataSet.shape[0]

    # 距离计算（使用欧式距离公式）
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
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


# 实现改进约会网站的配对效果
def file2matrix(fileName):
    fr = open(fileName)
    # 得到文件行数
    arrayLines = fr.readlines()
    numOfLines = len(arrayLines)
    # 创建返回的NumPy矩阵(以0填充的二维数组),numOfLines行,3列的数组
    returnMatrix = zeros((numOfLines, 3))
    classLabelVector = []
    index = 0

    # 解析文件数据到列表中
    for line in arrayLines:
        line = line.strip()  # 截取掉所有的回车字符
        listFromLine = line.split('\t')  # 使用\t将每行数据分割成一个元素列表
        returnMatrix[index, :] = listFromLine[0:3]  # 选取前三个元素,将它们存储到特征矩阵中
        classLabelVector.append(int(listFromLine[-1]))  # 将列表中的最后一列存储到向量classLabelVector中
        index += 1
    return returnMatrix, classLabelVector


# 使用Matploitlib创建散点图
def createMatplotlib(datingDataMat, datingLabels):
    fig = plt.figure()  # top level container for all plot elements
    ax = fig.add_subplot(111, facecolor='b')  # Add a subplot, 相当于 fig.add_subplot(1, 1, 1), facecolor表示背景色
    ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0 * array(datingLabels), 15.0 * array(datingLabels))  # 支持个性化标记散点图
    plt.show()


# 归一化特征值(用于处理不同范围内的特征值,降低不同特征值的严重影响)
# newValue = (oldValue - min) / (max - min)
def autoNum(dataSet):
    minVals = dataSet.min(0)  # 加上参数 0 使得函数可以从列中选取最小值,而不是选取当前行的最小值
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals  # 函数计算可能的取值范围
    normalDataSet = zeros(shape(dataSet))  # 创建新的返回矩阵
    m = dataSet.shape[0]
    #  使用tile将变量内容复制成输入矩阵同样大小的矩阵
    normalDataSet = dataSet - tile(minVals, (m, 1))
    normalDataSet = normalDataSet / tile(ranges, (m, 1))  # 具体特征值相除
    return normalDataSet, ranges, minVals


if __name__ == '__main__':
    group, labels = createDataSet()
    # print group
    # print labels

    # print classify0([0,0], group, labels, 3)

    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    # print datingDataMat
    # print datingLabels[0:20]

    # createMatplotlib(datingDataMat, datingLabels)

    norMat, ranges, minVals = autoNum(datingDataMat)
    print norMat
    print ranges
    print minVals