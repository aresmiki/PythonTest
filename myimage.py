# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 14:56:16 2018

@author: hl
"""

import numpy as np
import matplotlib as plt
import skimage as ski
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
def HardImage(a,b,im1,ys):
    HM=np.zeros(im1.shape,dtype=np.uint8)
    if ys==0:
        thresh = ski.filters.threshold_otsu(im1)
        binary = im1 > thresh
        HM=(np.ones(im1.shape,dtype=np.uint8)*255)*binary    
    else:
        HM=(np.ones(im1.shape,dtype=np.uint8)*255)*((im1>=a)&(im1<=b))
        """
        for i in range(im1.shape[0]-1):
            for j in range(im1.shape[1]-1):
                if (im1[i,j]<=max(a,b) & im1[i,j]>=min(a,b)):
                    HM[i,j]=255;
                else:
                    pass
        """
    return HM

"""
图像大小缩放
"""

def ImageResize(im1,a,b):
    m=im1.shape[0]
    n=im1.shape[1]
    im2=np.zeros([a,b],dtype=np.uint8)
    for j in range(a):
        sx=np.int(np.fix((j*m)/a))
        for i in range(b):
            if (i==0)|(j==0):
              pass
            else:
              sy=np.int(np.fix((i*n)/b))
           #   print([sx,sy])
              im2[j][i]=im1[sx][sy]    
    return im2


"""
边界区域连通性查询
"""
def LianTong(temp,a,b):
    rrbw=np.array(temp[:][:])
    if a==0 and b==0:
        pass
    else:
        rrbw[a:-a][b:-b]=1
    psi=np.ones(rrbw.shape,dtype=np.uint8)
    for i in range(rrbw.shape[0]):
        for j in range(rrbw.shape[1]):
            if rrbw[i][j]==0:
                psi[i][j]=0
            else:
                break
    
    for i in range(rrbw.shape[0]):
        for j in range(rrbw.shape[1]):
            if rrbw[i][rrbw.shape[1]-1-j]==0:
                psi[i][rrbw.shape[1]-1-j]=0
            else:
                break
    
    for j in range(rrbw.shape[1]):
        for i in range(rrbw.shape[0]):
            if rrbw[i][j]==0:
                psi[i][j]=0
            else:
                break
    for j in range(rrbw.shape[1]):
        for i in range(rrbw.shape[0]):
            if rrbw[rrbw.shape[0]-1-i][j]==0:
                psi[rrbw.shape[0]-1-i][j]=0
            else:
                break
    
    k=0
    while np.abs((np.sum(psi)-k))>0:
        k=np.sum(psi)
        for m in range(psi.shape[0]):
            for n in range(psi.shape[1]): 
                i=[m,n]
                if psi[i[0]][i[1]]==0:
                    t1=min(i[0]+1,rrbw.shape[0]-1)
                    t2=min(i[1]+1,rrbw.shape[1]-1)
                    t3=max(i[0]-1,0)
                    t4=max(i[1]-1,0)
                    if rrbw[t1][i[1]]==0:
                        psi[t1][i[1]]=0
                    if rrbw[i[0]][t2]==0:
                        psi[i[0]][t2]=0
                    if rrbw[t1][t2]==0:
                        psi[t1][t2]=0
                    if rrbw[t3][i[1]]==0:
                        psi[t3][i[1]]=0
                    if rrbw[i[0]][t4]==0:
                        psi[i[0]][t4]=0   
                    if rrbw[t3][t4]==0:
                        psi[t3][t4]=0
                    if rrbw[t1][t4]==0:
                        psi[t1][t4]=0
                    if rrbw[t3][t2]==0:
                        psi[t3][t2]=0
                    else:
                        pass
    return psi




