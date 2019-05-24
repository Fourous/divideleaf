import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def forhandle(x):
    # df = pd.read_csv(str, dtype=float, delimiter=',')
    # matrix = df.values
    # matrix = np.delete(matrix, 0, axis=1)
    # x=matrix[:,8:12]
    temp=PCA(n_components=3)
    newdata=temp.fit_transform(x)
    """
    对于4个特征向量，其中
    降维后的主成分方差值为:[4.27,0.118,0.00146]
    贡献率:[0.927,0.0269,0.0003322]
    第一个占据绝对要素
    """
    # print("降维后各主成分方差值\n", temp.explained_variance_)
    # print("个主成分贡献率\n", temp.explained_variance_ratio_)
    # print(newdata)
    return newdata



# 入口函数
# if __name__=='__main__':
#     print(forhandle('leaf.csv'))