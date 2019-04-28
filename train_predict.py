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
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colors
from sklearn.model_selection import train_test_split
def show_accuracy(y_hat, y_test, param):
    pass

def traindata(str):
    df=pd.read_csv(str)
    print(df)
    matrix=df.values
    print(matrix)
    print(matrix.shape)
    matrix=np.delete(matrix,0,axis=1)
    print(matrix)
    print(matrix.shape)
    x,y=np.split(matrix, (12, ), axis=1)
    x = x[:, :2]
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, train_size=0.6)
    clf = svm.SVC(C=0.8, kernel='rbf', gamma=20, decision_function_shape='ovr')
    clf.fit(x_train, y_train.ravel())
    print(clf.score(x_train,y_train))
    y_hat=clf.predict(x_train)
    show_accuracy(y_hat, y_train, '训练集')
    print(clf.score(x_test, y_test))
    y_hat = clf.predict(x_test)
    show_accuracy(y_hat, y_test, '测试集')

if __name__ == "__main__":
    traindata('leaf.csv')

