# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 14:56:16 2018

@author: hl
"""

import numpy as np
import matplotlib as plt

"""
L模式图像转换为RGB图像，并显示
该模式显示效果和图片浏览器相同
"""
def my_image_show(im1):
    
    imview=np.array([im1,im1,im1])
    imview=imview.swapaxes(1,0)  #改变轴位置
    imview=imview.swapaxes(2,1)  #改变轴位置
    plt.pyplot.figure()
    plt.pyplot.imshow(imview)
    plt.pyplot.axis('off')
    plt.pyplot.show()
    return

"""
图像灰度直方图统计
"""

def CalHist(im1):
    NumHist=np.zeros(256)
    for i in range(im1.shape[0]-1):
        for j in range(im1.shape[1]-1):
            NumHist[im1[i,j]]=NumHist[im1[i,j]]+1;
    NumHist=NumHist/NumHist.size
    return np.array([np.array(range(256)),NumHist])

"""
硬阈值处理图像,保留一定灰度值范围内的图像，并二值化
"""
def HardImage(a,b,im1):
    HM=np.zeros(im1.shape,dtype=np.uint8)
    for i in range(im1.shape[0]-1):
        for j in range(im1.shape[1]-1):
            if (im1[i,j]<=max(a,b) & im1[i,j]>=min(a,b)):
                HM[i,j]=255;
            else:
                pass
    return HM


