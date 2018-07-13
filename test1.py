# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 13:56:04 2018

@author: hl
"""

import numpy as np
import matplotlib as plt
import myimage as myim
import skimage as ski

#from skimage import filter,segmentation,measure,morphology,color

"""
read image from folder

"""
im1=plt.pyplot.imread('G:/4C/03ganhao/015801242_K1597131_0001_5_03.jpg')
"""
绘图
"""
myim.my_image_show(im1)
"""
直方图统计
"""
hist=myim.CalHist(im1)
plt.pyplot.figure('Hist')
plt.pyplot.hist(hist[1,:],hist[0,:])
plt.pyplot.show()

"""
硬阈值处理，图形二值化
"""
hw=myim.HardImage(200,255,im1)
myim.my_image_show(hw)

"""
形态学操作
"""
bw=ski.morphology.closing(hw,ski.morphology.square(10)) #闭运算
myim.my_image_show(bw)

""""""
bwt=(bw>200)*1
bwt.dtype=np.uint8;

labels=ski.measure.label(bw,ski.connectivity=2)  #8连通区域标记
dst=color.label2rgb(labels)  #根据不同的标记显示不同的颜色
print('regions number:',labels.max()+1)  #显示连通区域块数(从0开始标记)

plt.pyplot.figure(), (ax1, ax2) = plt.pyplot.subplots(1, 2)
ax1.imshow(bw, plt.cm.gray, interpolation='nearest')
ax1.axis('off')
ax2.imshow(dst,interpolation='nearest')
ax2.axis('off')

fig.tight_layout()
plt.show()











