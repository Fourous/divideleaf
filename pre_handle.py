# 这里进行预处理步骤
import numpy as np
import cv2 as cv
#灰度处理，采用加权平均法得方式进行处理
def grayhandle(str):
    testimg=cv.imread(str,1)
    img_info=testimg.shape
    #print(img_info)
    # (1200,1600,3)
    image_height=img_info[0]
    image_width=img_info[1]
    dst=np.zeros((image_height,image_width,3),np.uint8)
    for i in range(image_height):
        for j in range(image_width):
            (b,g,r)=testimg[i][j]
            gray=0.299*int(b)+0.587*int(g)+0.114*int(r)
            dst[i,j]=np.uint8(gray)
            #进行灰度化，主要是RGB三个分量得变化
    return dst;
#调用函数
#print(grayhandle('image/test.jpg'));
#cv.imshow('gray',grayhandle('image/test.jpg'));
#cv.waitKey(0);
#这里维数很高，矩阵形式显示

#图像二值化,输入灰度化的矩阵，输出二值化矩阵
#这里是直接调用的方法实现，并且输入的图像必须是灰度图像
def binaryhandle(str):
    img=cv.imread(str)
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary=cv.threshold(gray, 0, 255, cv.THRESH_OTSU)
    print(binary.shape)
    '''
    for i in  range(binary.shape[0]):
        for j in range(binary.shape[1]):
            if binary[i][j]==0:
                binary[i][j]=255;
            else:
                binary[i][j] = 0;
    cv.namedWindow('binary',0)
    cv.imshow('binary',binary);
    cv.waitKey(0)
    '''
    return binary;

#gamma校正
def gammahandle(str):
    img=str;
    img1 = np.power(img / float(np.max(img)), 1 / 1.5)
    img2 = np.power(img / float(np.max(img)), 1.5)
    cv.imshow('gamma1',img1);
    cv.imshow('gamma2',img2);
    cv.imshow('src',img)
    cv.waitKey(0)
    return;

#print(grayhandle('image/test.jpg'));
#cv.imshow('gray',grayhandle('image/test.jpg'));
#cv.waitKey(0);
if __name__ == "__main__":
    cv.namedWindow("gray", 0)
    # cv.resizeWindow("gray", 640, 480);
    cv.imshow('gray',binaryhandle('sone.tif'));
    cv.waitKey(0);

