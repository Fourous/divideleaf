"""

'Contrast' :    对比度  返回整幅图像中像素和它相邻像素之间的亮度反差。取值范围：[0,（GLCM行数-1）^2]。灰度一致的图 像，对比度为0。
'Correlation' : 相关    返回整幅图像中像素与其相邻像素是如何相关的度量值。取值范围：[-1,1]。灰度一致的图像，相关性为NaN。
'Energy' :      能量    返回GLCM中元素的平方和。取值范围：[0 1]。灰度一致的图像能量为1。
'Homogemeity' : 同质性  返回度量GLCM中元素的分布到对角线紧密程度。取值范围：[0 1]。对角矩阵的同质性为1。

"""
import cv2
import math

# 定义最大灰度级数
gray_level = 16
def maxGrayLevel(img):
    max_gray_level = 0
    (height, width) = img.shape
    print
    height, width
    for y in range(height):
        for x in range(width):
            if img[y][x] > max_gray_level:
                max_gray_level = img[y][x]
    return max_gray_level + 1


def getGlcm(input, d_x, d_y):
    srcdata = input.copy()
    ret = [[0.0 for i in range(gray_level)] for j in range(gray_level)]
    (height, width) = input.shape
    max_gray_level = maxGrayLevel(input)
    # 若灰度级数大于gray_level，则将图像的灰度级缩小至gray_level，减小灰度共生矩阵的大小
    if max_gray_level > gray_level:
        for j in range(height):
            for i in range(width):
                srcdata[j][i] = srcdata[j][i] * gray_level / max_gray_level

    for j in range(height - d_y):
        for i in range(width - d_x):
            rows = srcdata[j][i]
            cols = srcdata[j + d_y][i + d_x]
            ret[rows][cols] += 1.0

    for i in range(gray_level):
        for j in range(gray_level):
            ret[i][j] /= float(height * width)

    return ret


def feature_computer(p):
    Con = 0.0
    Eng = 0.0
    Asm = 0.0
    Idm = 0.0
    for i in range(gray_level):
        for j in range(gray_level):
            Con += (i - j) * (i - j) * p[i][j]
            Asm += p[i][j] * p[i][j]
            Idm += p[i][j] / (1 + (i - j) * (i - j))
            if p[i][j] > 0.0:
                Eng += p[i][j] * math.log(p[i][j])
    return Asm, Con, -Eng, Idm


# def test(image_name):
#     img = cv2.imread(image_name)
#     try:
#         img_shape = img.shape
#     except:
#         print
#         'imread error'
#         return
# #双斜杠表示整数除法
#     img = cv2.resize(img, (img_shape[1]//2, img_shape[0]//2), interpolation=cv2.INTER_CUBIC)
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     glcm_0 = getGlcm(img_gray, 1, 0)
#     glcm_1=getGlcm(img_gray, 0, 1)
#     glcm_2=getGlcm(img_gray, 1, 1)
#     glcm_3=getGlcm(img_gray, -1, 1)
#     asm0, con0, eng0, idm0 = feature_computer(glcm_0)
#     asm1, con1, eng1, idm1 = feature_computer(glcm_1)
#     asm2, con2, eng2, idm2 = feature_computer(glcm_2)
#     asm3, con3, eng3, idm3 = feature_computer(glcm_3)
#     return [asm0, con0, eng0, idm1, asm1, con1, eng1, idm2, asm2, con2, eng2, idm2, asm3, con3, eng3, idm3]

def glcminthis(img_gray):
    glcm_0 = getGlcm(img_gray, 1, 0)
    glcm_1 = getGlcm(img_gray, 0, 1)
    glcm_2 = getGlcm(img_gray, 1, 1)
    glcm_3 = getGlcm(img_gray, 1, 2)
    asm0, con0, eng0, idm0 = feature_computer(glcm_0)
    asm1, con1, eng1, idm1 = feature_computer(glcm_1)
    asm2, con2, eng2, idm2 = feature_computer(glcm_2)
    asm3, con3, eng3, idm3 = feature_computer(glcm_3)
    return [asm0, con0, eng0, idm1, asm1, con1, eng1, idm2, asm2, con2, eng2, idm2, asm3, con3, eng3, idm3]