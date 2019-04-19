"""

形状特征提取，提取出八个描述子
1）周长凹凸比：CP=D/Dt
2）面积凹凸比：CA=S/St
3）形状参数：F=4πS/D²
4）圆形度：C= D²/S
5）狭长度：N=L/W
6）矩形度：R=S/L×W
7）周长长度比：PRP=D/（L+W）
8）偏心率：e=√(1−(𝑊/2)"²" /(𝐿/2)"²" )
D为周长，计算边缘的像素点实现，通过计算个数表示周长
S为面积，在预处理过后的图像中计算黑色像素点的个数来实现
L W为叶片的长短轴，这个是相互垂直的，先找出叶片最长轴，然后找到垂直线能够延伸到叶片边缘为最短轴
凸包提取通过算法QuickHull实现，所谓凸包就是能够包围这个图像，计算周长和面积和上面类似

主要难点：提取周长，面积，长短轴，QuickHull凸包计算
"""
import numpy as np
import cv2 as cv
import pre_handle as pre

pre.binaryhandle('image/test.jpg')
