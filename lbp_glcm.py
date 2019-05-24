import glcm_extract as glcm
from LBP_extract import *
import pandas as pd
import os
import numpy as np
import time
import  csv

def handleall(image):
    lbp = LBP()
    lbparray=lbp.lbphandle(image)
    allarr=glcm.glcminthis(lbparray)
    print(allarr)
    return allarr

# def create_csv():
#     print("****")
#     pd.read_csv('lbp_glcm.csv',header=None,names=["asm0","con0","eng0","idm0","asm1","con1","eng1","idm1","asm2","con2","eng2","idm2","asm3","con3","eng3","idm3"])
#     return 1;

def add(list):
    df = pd.DataFrame(columns=("asm0","con0","eng0","idm0","asm1","con1","eng1","idm1","asm2","con2","eng2","idm2","asm3","con3","eng3","idm3"))
    df.loc['one'] = list

def gerneratefile(str):
    list=[]
    list.append(handleall(str))
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
    return matrix

def create_csv():
    path = "lbp_glcm.csv"
    with open(path,'w') as f:
        csv_write = csv.writer(f)
        csv_head = ["asm0", "con0", "eng0", "idm0", "asm1", "con1", "eng1", "idm1", "asm2", "con2", "eng2", "idm2", "asm3", "con3", "eng3", "idm3", "divide"]
        csv_write.writerow(csv_head)

def addonedata(list):
    # columns = ["asm0", "con0", "eng0", "idm0", "asm1", "con1", "eng1", "idm1", "asm2", "con2", "eng2", "idm2", "asm3","con3", "eng3", "idm3", "divide"]
    path = "lbp_glcm.csv"
    with open(path,'a+') as f:
        csv_write=csv.writer(f)
        data_row = list
        csv_write.writerow(data_row)

if __name__ == '__main__':
    start = time.perf_counter()
    file = pd.read_csv("lbp_glcm.csv")
    getdir = reverselist('image/divide/')
    # getdir得结构是
    # [['one', 'two'], [['test/one/test.jpg', 'test/one/test1.jpg'], ['test/two/test1.jpg']]]
    # 第一个是类别名称第二个是数组具体名称
    listdiv = getdir[0]  # 类别名称list['one','two']
    # listtemp = gerneratefile(getdir[1][0][0])
    # print(listtemp[0])
    # print(listdiv[0])
    # listtemp[0].append(listdiv[0][0])  # 序列记录，也就是类别记录
    # print(listtemp[0])
    for m in range(len(listdiv)):
        for n in range(len(getdir[1][m])):
            try:
                listtemp = gerneratefile(getdir[1][m][n])
                listtemp[0].append(listdiv[m])  # 序列记录，也就是类别记录
                print(listtemp[0])
                addonedata(listtemp[0])
            except Exception as e:
                pass
            continue
    elapsed = (time.perf_counter() - start)
    print("time used:", elapsed)