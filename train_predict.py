'''
这里读取出CSV文件后开始训练
'''
import os
import numpy as np
from pandas import Series,DataFrame
import pandas as pd
import hog_extract as hx
import glcm_extract as gx
from sklearn import svm
import time
import newPCA as lowp
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colors
from sklearn import model_selection

def traindata(str):
    start = time.perf_counter()
    df=pd.read_csv(str, dtype=float, delimiter=',')
    matrix = df.values
    matrix = np.delete(matrix, 0, axis=1)
    x,y=np.split(matrix, (12, ), axis=1)
    # 这里的形状特征提取有问题，导致分类不准确，尽快完成形状特征的提取，肯定是有问题的
    x = x[:, 8:12]
    # x=lowp.forhandle(x)
    # print("降维后的数据:\n",x)
    y=y.astype(np.int)
    # x:train_data 划分样本特征集，y:train_target划分样本结果，testsize样本占比，random_state随机种子
    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, random_state=1, test_size=0.3)
    clf = svm.SVC(C=0.7, kernel='rbf', gamma=20, decision_function_shape='ovr')
    clf.fit(x_train, y_train.ravel())

    def show_accuracy(y_hat, y_train, param):
        pass

    print("SVM输出训练集准确率为:\n",clf.score(x_train, y_train))
    y_hat = clf.predict(x_train)
    show_accuracy(y_hat, y_train, '训练集')
    print("SVM输出测试集准确率为:\n",clf.score(x_test, y_test))
    y_hat = clf.predict(x_test)
    show_accuracy(y_hat, y_test, '测试集')
    # print("decision_function:\n",clf.decision_function(x_train))
    # print("\npredict:\n",clf.predict(x_train))
    # 可视化处理
    # x1_min, x1_max = x[:, 0].min(), x[:, 0].max()  # 第0列的范围
    # x2_min, x2_max = x[:, 1].min(), x[:, 1].max()  # 第1列的范围
    # x1, x2 = np.mgrid[x1_min:x1_max:200j, x2_min:x2_max:200j]  # 生成网格采样点
    # grid_test = np.stack((x1.flat, x2.flat), axis=1)  # 测试点
    # mpl.rcParams['font.sans-serif'] = [u'SimHei']
    # mpl.rcParams['axes.unicode_minus'] = False
    # cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
    # cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])
    # plt.pcolormesh(x1, x2,grid_test,cmap=cm_light)
    # plt.scatter(x[:, 0], x[:, 1], c=y, edgecolors='k', s=50, cmap=cm_dark)  # 样本
    # plt.scatter(x_test[:, 0], x_test[:, 1], s=120, facecolors='none', zorder=10)  # 圈中测试集样本
    # plt.xlabel(u'花萼长度', fontsize=13)
    # plt.ylabel(u'花萼宽度', fontsize=13)
    # plt.xlim(x1_min, x1_max)
    # plt.ylim(x2_min, x2_max)
    # plt.title(u'SVM二特征分类', fontsize=15)
    # plt.grid()
    # plt.show()
    elapsed = (time.perf_counter() - start)
    print("time used:", elapsed)

if __name__ == "__main__":
    traindata('leaf.csv')

