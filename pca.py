'''
Todo 主成分降维
'''
import os
import numpy as np
from pandas import Series,DataFrame
import pandas as pd
import hog_extract as hx
import glcm_extract as gx
from sklearn import svm
import time

def create_csv():
    print("****")
    pd.read_csv('leaf.csv',header=None,names=["CP","CA","F","C","N","R","PRP","e","asm","con","eng","idm"])
    return 1;

def add(list):
    df = pd.DataFrame(columns=("CP","CA","F","C","N","R","PRP","e","asm","con","eng","idm"))
    df.loc['one'] = list

def gerneratefile(str):
    list=[]
    list1=hx.calaround(str);
    list2=gx.test(str);
    for i in range(8):
        list.append(list1[i])
    for j in range(4):
        list.append(list2[j])
    print("*****打印生成参数名称")
    print(list)
    print(len(list))
    add(list)
    return list;

def reverselist(rootdir):
    list = os.listdir(rootdir)
    matrix=[]
    matrix.append(list)
    matrixtemp=[]
    # 这里将文件夹名存入数组，用pandas进行操作
    for filename in list:
        temp = []
        chiledir = 'image/divide/' + filename
        #print(chiledir)#分类类别，也作为文件名存在
        listchild = os.listdir(chiledir)
        for filedir in listchild:
            realdir = chiledir + '/' + filedir
            #print(realdir)  # 准确的文件路径
            temp.append(realdir)
        matrixtemp.append(temp)
    matrix.append(matrixtemp)
    return matrix;

if __name__ == "__main__":
    start=time.perf_counter()
    columns = ["CP", "CA", "F", "C", "N", "R", "PRP", "e", "asm", "con", "eng", "idm", "divide"]
    df = pd.DataFrame({}, columns=columns)#构造空的DataFram
    cout=0#总数需要计算出来
    list=[]
    getdir=reverselist('image/divide')
    listdiv=getdir[0]#类别名称

    for m in range(len(listdiv)):
            for n in range(len(getdir[1][m])):
                try:
                    listtemp = gerneratefile(getdir[1][m][n])
                    listtemp.append(m)  # 序列记录，也就是类别记录
                    list.append(listtemp)
                    cout += 1
                except Exception as e:
                    pass
                continue


    matrix = np.matrix(list)
    for i in range(cout):
        data = {
            'CP':  matrix[i, 0].tolist(),
            'CA':  matrix[i, 1].tolist(),
            'F':   matrix[i, 2].tolist(),
            'C':   matrix[i, 3].tolist(),
            'N':   matrix[i, 4].tolist(),
            'R':   matrix[i, 5].tolist(),
            'PRP': matrix[i, 6].tolist(),
            'E':   matrix[i, 7].tolist(),
            'ASM': matrix[i, 8].tolist(),
            'CON': matrix[i, 9].tolist(),
            'ENG': matrix[i,10].tolist(),
            'IDM': matrix[i,11].tolist(),
            'DIV': matrix[i,12].tolist(),
        }
        df = df.append(data, ignore_index=True)
    df.to_csv(path_or_buf='leaf.csv')


    # list1=[1,2,3,4,5,6,7,8,9,10]
    # list2=[11,12,13,14,15,16,17,18,19,20]
    # list.append(list1)
    # list.append(list2)
    #matrixnew=np.transpose(matrix)
    # matrixx=np.row_stack(gerneratefile('exchange/image/test.jpg'))
    # matrixx=np.row_stack(gerneratefile('exchange/image/test1.jpg'))
    #转置
    # listt=np.transpose(matrixx)
    # print(listt)
    # for i in range(len(listt)):
    #     listt[i].append("four")
    #按照列添加13列
    #建立字典data
    #建立空的DataFram

    #主要分类目录，divide目录作为主目录
    #读取所有文件，文件夹名称作为分类类别写入，12个参数作为特征写入，共13列,采用pandas的DataFrame操作
    #matrixx=reverselist('image/divide')
    #print(matrixx[1][0])

    #
    #这里不断新建DataFram

    elapsed=(time.perf_counter()-start)
    print("time used:",elapsed)













