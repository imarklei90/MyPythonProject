# -*- encoding: utf-8 -*-

'''
    基于kNN的手写识别系统
'''

from numpy import *
from os import listdir


# 实现kNN算法（使用kNN算法将每组数据划分到某个类中）
def classify0(inX, dataSet, labels, k):  # 用于分类的输入向量inX,输入的训练样本集,标签向量lables,选择最近邻居的数目
    # 训练集的维度
    data_set_size = dataSet.shape[0]

    # 距离计算（使用欧式距离公式）
    diff_mat = tile(inX, (data_set_size, 1)) - dataSet
    sq_diff_mat = diff_mat**2
    sq_distances = sq_diff_mat.sum(axis=1)
    distance = sq_distances ** 0.5

    # 选择距离最小的个点
    sorted_dist_indics = distance.argsort()
    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_dist_indics[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1

    # 排序
    sorted_class_count = sorted(class_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def img2vector(file_name):
    # 创建一个1 * 1024的向量
    return_vector = zeros((1,1024))
    fr = open(file_name)
    for i in range(32):
        line_str = fr.readline()
        for j in range(32):
            # 将32 * 32的二进制图像矩阵转换成1 * 1024的向量
            return_vector[0, 32*i + j] = int(line_str[j])
    return return_vector


# 测试
def handwritingClassTest():
    hw_lables = []
    # 获取目录内容
    trainingFileList = listdir('trainingDigits')
    # 获取目录中文件个数
    m = len(trainingFileList)
    # 创建一个m行1024列的矩阵,矩阵的每行存储一个图像
    trainingMat = zeros((m, 1024))
    for i in range(m):
        # 从文件名解析分类数字
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hw_lables.append(classNumStr)

        # 载入图像
        trainingMat[i, :] = img2vector('trainingDigits/%s' % fileNameStr)

    # 对testDigits执行相似操作
    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hw_lables, 3)
        print "the classifier came back with : %d, the real answer is : %d" %(classifierResult, classNumStr)
        if classifierResult != classNumStr:
            errorCount += 1.0
    print "\n the total number of errors is : %d" % errorCount
    print "\n the total error rate is: %f" %(errorCount/float(mTest))


if __name__ == '__main__':
    test_vector = img2vector('testDigits/0_13.txt')
    print test_vector[0, 0:31]