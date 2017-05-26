# -*- encoding:utf-8 -*-

'''
    kNN算法实现:
        对电影进行分类
        改进约会网站的效果
    使用Matplotlib创建散点图
    归一化数据
'''

from numpy import *
import operator
import matplotlib.pyplot as plt


# 创建数据集
def createDataSet():
    group = array([[1.0,1.1], [1.0,1.0], [0,0], [0,0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


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


# 实现改进约会网站的配对效果
def file2matrix(fileName):
    fr = open(fileName)
    # 得到文件行数
    array_lines = fr.readlines()
    num_of_lines = len(array_lines)
    # 创建返回的NumPy矩阵(以0填充的二维数组),numOfLines行,3列的数组
    return_matrix = zeros((num_of_lines, 3))
    class_label_vector = []
    index = 0

    # 解析文件数据到列表中
    for line in array_lines:
        line = line.strip()  # 截取掉所有的回车字符
        list_from_line = line.split('\t')  # 使用\t将每行数据分割成一个元素列表
        return_matrix[index, :] = list_from_line[0:3]  # 选取前三个元素,将它们存储到特征矩阵中
        class_label_vector.append(int(list_from_line[-1]))  # 将列表中的最后一列存储到向量classLabelVector中
        index += 1
    return return_matrix, class_label_vector


# 使用Matploitlib创建散点图
def createMatplotlib(datingDataMat, datingLabels):
    fig = plt.figure()  # top level container for all plot elements
    ax = fig.add_subplot(111, facecolor='b')  # Add a subplot, 相当于 fig.add_subplot(1, 1, 1), facecolor表示背景色
    ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0 * array(datingLabels), 15.0 * array(datingLabels))  # 支持个性化标记散点图
    plt.show()


# 归一化特征值(用于处理不同范围内的特征值,降低不同特征值的严重影响)
# newValue = (oldValue - min) / (max - min)
def autoNorm(dataSet):
    min_vals = dataSet.min(0)  # 加上参数 0 使得函数可以从列中选取最小值,而不是选取当前行的最小值
    max_vals = dataSet.max(0)
    ranges = max_vals - min_vals  # 函数计算可能的取值范围
    normal_data_set = zeros(shape(dataSet))  # 创建新的返回矩阵
    m = dataSet.shape[0]
    #  使用tile将变量内容复制成输入矩阵同样大小的矩阵
    normal_data_set = dataSet - tile(min_vals, (m, 1))
    normal_data_set = normal_data_set / tile(ranges, (m, 1))  # 具体特征值相除
    return normal_data_set, ranges, min_vals


# 分类器针对约会网站的测试
def datingClassTest():
    hi_ratio = 0.10
    # 从文件中读取值数据
    dating_data, dating_label = file2matrix('datingTestSet.txt')
    # 归一化特征值
    norm_mat, ranges, min_vals = autoNorm(dating_data)
    m = norMat.shape[0]
    # 计算测试向量的数量,确定哪些数据用于测试,哪些数据用于分类器的训练样本
    num_test_vces = int(m * hi_ratio)
    error_count = 0.0
    for i in range(num_test_vces):
        classifierResult = classify0(norm_mat[i:], norm_mat[num_test_vces:m, :], dating_label[num_test_vces:m], 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, dating_label[i])
        if classifierResult != dating_label[i]:
            error_count += 1.0
    print "the total error rate is : %f" % (error_count / float(num_test_vces))


if __name__ == '__main__':
    # group, labels = createDataSet()
    # print group
    # print labels

    # print classify0([0,0], group, labels, 3)

    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    print datingDataMat
    print datingLabels[0:20]

    createMatplotlib(datingDataMat, datingLabels)

    # norMat, ranges, minVals = autoNum(datingDataMat)
    # print norMat
    # print ranges
    # print minVals

    datingClassTest()