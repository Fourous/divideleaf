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
import math
square=1.414
Pi=3.1415

def edgeline(str):
    kernal=cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    #腐蚀操作
    dilate_img=cv.dilate(str,kernal)
    erode_img=cv.erode(str,kernal)
    absdiff_img=cv.absdiff(dilate_img,erode_img);
    retval,threshold_img=cv.threshold(absdiff_img,0,255,cv.THRESH_BINARY);
    result=cv.bitwise_not(threshold_img);
    #cv.namedWindow('result',0);
    #cv.imshow('result',result);
    #cv.waitKey(0);
    return result;

#计算链码
def Freeman(str):
    original=cv.imread(str)
    img=edgeline(pre.binaryhandle(str))
    contours, hierarchy = cv.findContours(img,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    cv.drawContours(original,contours[2],-1,(0,0,255),3)
    #cv.namedWindow('img',0)
    #cv.imshow('img',original)
    #cv.waitKey(0)
    print (type(contours[2]))
    print("轮廓总数为")
    print(np.size(contours))
    print(len(contours))
    print (len(contours[2]))
    lengh=len(contours[2])
    columns = []
    for i in range(lengh):
        columns.append(contours[2][i] - contours[2][i - 1])
    print("打印conlum")
    print(columns)
    print(columns[0])
    print (len(columns))
    print (columns[1][0][0])
    a = []
    for i in range(lengh):
        if columns[i][0][0] == 0 and columns[i][0][1] == -1:
            a.append(6)
        elif columns[i][0][0] == 0 and columns[i][0][1] == 1:
            a.append(2)
        elif columns[i][0][0] == 1 and columns[i][0][1] == 1:
            a.append(1)
        elif columns[i][0][0] == 1 and columns[i][0][1] == 0:
            a.append(0)
        elif columns[i][0][0] == 1 and columns[i][0][1] == -1:
            a.append(7)
        elif columns[i][0][0] == -1 and columns[i][0][1] == 1:
            a.append(3)
        elif columns[i][0][0] == -1 and columns[i][0][1] == 0:
            a.append(4)
        elif columns[i][0][0] == -1 and columns[i][0][1] == -1:
            a.append(5)
    print(a)
    return a;

#返回轮廓数组
def around(str):
    original = cv.imread(str)
    img = edgeline(pre.binaryhandle(str))
    contours, hierarchy = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    cv.drawContours(original, contours[2], -1, (0, 0, 255), 3)
    #cv.namedWindow('img', 0)
    #cv.imshow('img', original)
    #cv.waitKey(0)
    print(type(contours[2]))
    return contours[2];


#计算周长
def circumference(a):
    length=len(a)
    cir=0
    for i in range(length):
        if a[i]%2==0:
            cir+=square;
        else :
            cir+=1;
    return cir;

#计算面积,通过计算黑色像素点的个数得到
def Area(str):
    blacknum=0;
    img=pre.binaryhandle(str)
    #cv.imshow('img',img)
    #cv.waitKey(0)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j]==0:
                blacknum+=1;#计算时间大概3s左右一张图
    return blacknum;

#quickhull算法求凸包
def quickHull(str):
    original=cv.imread(str)
    img = edgeline(pre.binaryhandle(str))
    contours, hierarchy = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    cv.drawContours(original, contours[2], -1, (0, 0, 255), 3)
    img=contours[2]
    hull=cv.convexHull(img)
    print(hull)
    list=[]
    length=len(hull)
    for i in range(length):
        cv.line(original,tuple(hull[i][0]),tuple(hull[(i+1)%length][0]),(0,0,0),2)
        list.append(hull[i][0])
    #cv.namedWindow('hull',0)
    #cv.imshow('hull',original)
    #cv.waitKey(0)
    print(hull.shape)
    return list;

def savaimg(str):
    img = cv.imread(str)
    strname='exchange/'+str
    print(img.shape)
    back = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    back.fill(255)
    hull = quickHull(str)
    length = len(hull)
    for i in range(length):
        cv.line(back, tuple(hull[i][0]), tuple(hull[(i + 1) % length][0]), (0, 0, 0), 2)
    cv.imwrite(strname, back);
    return strname;

#外接凸包的周长,这里逻辑是准备先连接凸包，还是计算链码方式计算
def tcircumference(str):
    #Todo 求解凸包的周长，这里一定有简便方法
    perimeter=0
    points=quickHull(str)
    for i in range(0, len(points) - 1):
        lenper=math.sqrt((points[i][0] - points[(i+1)%(len(points))][0])**2 + (points[i][1] - points[(i+1)%(len(points))][1])**2)
        perimeter+=lenper
    return perimeter;

#外接凸包的面积
def tArea(str):
    points=quickHull(str)
    #Todo 求解凸包的面积
    #基于向量叉乘计算多边形面积
    area = 0
    if (len(points) < 3):
        raise Exception("error")

    for i in range(0, len(points) - 1):
        p1 = points[i]
        p2 = points[i + 1]
        triArea = (p1[0] * p2[1] - p2[0] * p1[1]) / 2
        # print(triArea)
        area += triArea

    fn = (points[-1][0] * points[0][1] - points[0][0] * points[-1][1]) / 2
    # print(fn)
    return abs(area + fn)

#计算最小外接矩形
def boxhandle(str):
    img = cv.imread(str)
    coutour = around(str)
    rect = cv.minAreaRect(coutour)
    # 中心坐标
    print(rect)
    box = cv.boxPoints(rect)
    box = np.int0(box)
    print(box)
    for i in range(4):
        cv.line(img, tuple(box[i]), tuple(box[(i + 1) % 4]), (0, 0, 0), 2)
    #cv.namedWindow('imgname', 0)
    #cv.imshow('imgname', img)
    #cv.waitKey(0)
    x, y = rect[0]
    cv.circle(img, (int(x), int(y)), 3, (0, 255, 0), 5)
    # 长宽总有width>height
    width, height = rect[1]
    # 角度:[-90,0]
    angle = rect[2]
    print('width=', width, 'height=', height, 'x=', x, 'y=', y, 'angle=', angle)
    return rect[1]
#计算长轴
def longdist(str):
    #长轴也就是最小外接矩形的长
    width,height=boxhandle(str)
    return width;
#计算短轴
def shortdist(str):
    # 短轴也就是最小外接矩形的高
    width, height = boxhandle(str)
    return height;

#test区域
def calaround(str):
    '''
Todo
1）周长凹凸比：CP=D/Dt
2）面积凹凸比：CA=S/St
3）形状参数：F=4πS/D²
4）圆形度：C= D²/S
5）狭长度：N=L/W
6）矩形度：R=S/L×W
7）周长长度比：PRP=D/（L+W）
8）偏心率：e=√(1−(𝑊/2)"²" /(𝐿/2)"²" )
    '''
    #基本数据，最后返回需要是float类型
    D=circumference(Freeman(str));
    S=Area(str);
    Dt=tArea(str);
    St=tcircumference(str);
    CP=D/Dt;
    CA=S/St;
    L=longdist(str);
    W=shortdist(str);
    F=4*Pi*S/D**2
    C=D**2/S
    N=L/W
    R=S/L*W
    PRP=D/(L+W)
    e=(((1-(W/2))**2)/((L/2)**2))**0.5
    return [CP,CA,F,C,N,R,PRP,e]
#toge=around('image/test.jpg')
#print(toge.shape)
print(calaround('image/test.jpg'))