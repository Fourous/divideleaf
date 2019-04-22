'''
Todo 主成分降维
'''
import numpy as np
import pandas as pd
import hog_extract as hx
import glcm_extract as gx
import csv
def create_csv():
    df_example_noCols = pd.read_csv("leaf.csv", header=None,sep='tab')
    #pd.read_csv("leaf.csv", header=None, names=["CP","CA","F","C","N","R","PRP","e","asm","con","eng","idm"])
    df_example_noCols.columns = ["CP","CA","F","C","N","R","PRP","e","asm","con","eng","idm"]
    return 1;

def gerneratefile(str):
    list=[]
    list.append(hx.calaround(str));
    list.append(gx.test(str));
    print("*****打印生成参数名称")
    print(list)
    print(len(list))
    return list;

if __name__ == "__main__":
    create_csv()





