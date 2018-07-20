# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 13:56:04 2018

@author: hl
"""
 
import numpy as np
import matplotlib as plt
import myimage as myim
from skimage import morphology
from skimage import feature
import skimage as ski 
import matplotlib.patches as mpatches
from skimage.transform import (hough_line, hough_line_peaks,
                               probabilistic_hough_line)

#from skimage import filter,segmentation,measure,morphology,color


"""
read image from folder

"""
#im1=plt.pyplot.imread('G:/4C/03ganhao/020044923_K1600416_0147_5_03.jpg')
#im1=plt.pyplot.imread('G:/4C/03ganhao/020000676_K1599538_0105_5_03.jpg')
#im1=plt.pyplot.imread('G:/4C/03ganhao/020145593_K1601721_0207_5_03.jpg')
im1=plt.pyplot.imread('G:/4C/03ganhao/020131466_K1601421_0195_5_03.jpg')


"""
绘图
"""
myim.my_image_show(im1)
"""
直方图统计
"""
"""
hist=myim.CalHist(im1)
plt.pyplot.figure('Hist')
plt.pyplot.hist(hist[1,:],hist[0,:])
plt.pyplot.show()
"""
"""
硬阈值处理，图形二值化,最后参数为零时，二值化阈值采用大津方法
"""
hw=myim.HardImage(150,255,im1,1)
#myim.my_image_show(hw)

"""
形态学操作
"""

bw=morphology.closing(hw,morphology.square(20)) #闭运算 
#myim.my_image_show(bw)

""""""
labels=ski.measure.label((bw>1),connectivity=2)  #8连通区域标记
dst=ski.color.label2rgb(labels)  #根据不同的标记显示不同的颜色
#print('regions number:',labels.max()+1)  #显示连通区域块数(从0开始标记)

"""
plt.pyplot.figure()
plt.pyplot.subplot(121)
plt.pyplot.imshow(bw, plt.cm.gray, interpolation='nearest')
plt.pyplot.axis('off')
plt.pyplot.subplot(122)
plt.pyplot.imshow(dst,interpolation='nearest')
plt.pyplot.axis('off')
"""

fig, ax = plt.pyplot.subplots(figsize=(10, 6))
ax.imshow(dst)

for region in ski.measure.regionprops(labels):
    # 绘制大于面积100的联通区域
    if region.area >= 100:
        # 绘制一个正方形框上目标，并输出区域内图像
        minr, minc, maxr, maxc = region.bbox
        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                  fill=False, edgecolor='b', linewidth=2)
        ax.add_patch(rect)
        rhw=hw[minr-5:maxr+5,minc-10:maxc+10]
        rbw=bw[minr-5:maxr+5,minc-10:maxc+10]
        #print([minr, minc, maxr, maxc])        
ax.set_axis_off()
plt.pyplot.tight_layout()
plt.pyplot.show()

#rbw=bw[:]
#rhw=hw[:]

#myim.my_image_show(rbw)

"""
rhw=morphology.dilation(rhw,morphology.square(3))
myim.my_image_show(rhw)
"""
edges=feature.canny(rbw, sigma=0.5,low_threshold=0.55, high_threshold=0.8)
plt.pyplot.figure()
plt.pyplot.imshow(edges, cmap=plt.cm.gray)

# hough tansform

rbw=edges*1

h, theta, d = hough_line(rbw)

# Generating figure 1
fig, axes = plt.pyplot.subplots(1, 3, figsize=(15, 6))
ax = axes.ravel()
ax[0].imshow(rbw, cmap=plt.cm.gray)
ax[0].set_title('Input image')
ax[0].set_axis_off()

ax[1].imshow(np.log(1 + h),
             extent=[np.rad2deg(theta[-1]), np.rad2deg(theta[0]), d[-1], d[0]],
             cmap=plt.cm.gray, aspect=1/1.5)
ax[1].set_title('Hough transform')
ax[1].set_xlabel('Angles (degrees)')
ax[1].set_ylabel('Distance (pixels)')
ax[1].axis('image')

ax[2].imshow(rbw, cmap=plt.cm.gray)
lines=[]
for _, angle, dist in zip(*hough_line_peaks(h, theta, d,min_distance=20,min_angle=20,threshold=0.2*np.max(h))):
    y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
    y1 = (dist - rbw.shape[1] * np.cos(angle)) / np.sin(angle)
    ax[2].plot((0, rbw.shape[1]), (y0, y1), '-r')  
    lines.append({'angle':angle,'minx':0,'miny':y0,'maxx':rbw.shape[1],'maxy':y1,'rate':-1/np.tan(angle)})
ax[2].set_xlim((0, rbw.shape[1]))
ax[2].set_ylim((rbw.shape[0], 0))
ax[2].set_axis_off()
ax[2].set_title('Detected lines')

lines=sorted(lines,key=lambda i:i['angle'])

coner=[]
xcon=-(lines[0]['miny']-lines[0]['rate']*lines[0]['minx']-lines[2]['miny']+lines[2]['rate']*lines[2]['minx'])/(lines[0]['rate']-lines[2]['rate'])
ycon=lines[0]['rate']*xcon+lines[0]['miny']-lines[0]['rate']*lines[0]['minx']
coner.append([xcon,ycon])
xcon=-(lines[1]['miny']-lines[1]['rate']*lines[1]['minx']-lines[2]['miny']+lines[2]['rate']*lines[2]['minx'])/(lines[1]['rate']-lines[2]['rate'])
ycon=lines[1]['rate']*xcon+lines[1]['miny']-lines[1]['rate']*lines[1]['minx']
coner.append([xcon,ycon])
xcon=-(lines[0]['miny']-lines[0]['rate']*lines[0]['minx']-lines[3]['miny']+lines[3]['rate']*lines[3]['minx'])/(lines[0]['rate']-lines[3]['rate'])
ycon=lines[0]['rate']*xcon+lines[0]['miny']-lines[0]['rate']*lines[0]['minx']
coner.append([xcon,ycon])
xcon=-(lines[1]['miny']-lines[1]['rate']*lines[1]['minx']-lines[3]['miny']+lines[3]['rate']*lines[3]['minx'])/(lines[1]['rate']-lines[3]['rate'])
ycon=lines[1]['rate']*xcon+lines[1]['miny']-lines[1]['rate']*lines[1]['minx']
coner.append([xcon,ycon])

coner=sorted(coner)
if coner[0][1]>coner[1][1]:
    t=coner[0]
    coner[0]=coner[1]
    coner[1]=t
else:
    pass
if coner[2][1]>coner[3][1]:
    t=coner[2]
    coner[2]=coner[3]
    coner[3]=t
else:
    pass
for i in coner:
    ax[2].plot(i[0],i[1], '*b')



fig,axm=plt.pyplot.subplots(1,2)
ax = axm.ravel()
ax[0].imshow(rhw,cmap=plt.cm.gray)
ax[0].set_axis_off()
ax[1].imshow(rhw, cmap=plt.cm.gray)
for i in lines:
    ax[1].plot((i['minx'], i['maxx']), (i['miny'], i['maxy']), '-r')  
for i in coner:
    ax[1].plot(i[0],i[1], '*b')
ax[1].plot(0,0,'*r')
ax[1].set_xlim((0, rhw.shape[1]))
ax[1].set_ylim((rhw.shape[0], 0))
ax[1].set_axis_off()

#图像矫正旋转     
src = np.array([[0, 0], [0, rhw.shape[0]], [rhw.shape[1],rhw.shape[0]], [rhw.shape[1], 0]])
dst = np.array([np.fix(coner[0]), np.fix(coner[1]), np.fix(coner[3]), np.fix(coner[2])])

tform3 = ski.transform.ProjectiveTransform()
tform3.estimate(src, dst)
warped = ski.transform.warp(rhw, tform3,output_shape=(rhw.shape[0], rhw.shape[1]))
#plt.pyplot.figure()
#plt.pyplot.imshow(warped,cmap=plt.cm.gray)

"""
将像素大小统一
"""

rwarped=myim.ImageResize(warped,105,170)

"""
plt.pyplot.subplot(1,2,1)
plt.pyplot.axis([0,np.max([warped.shape[1],rwarped.shape[1]]),np.max([warped.shape[0],rwarped.shape[0]]),0])
plt.pyplot.axis('off')
plt.pyplot.title('Origin')
plt.pyplot.imshow(warped,cmap=plt.cm.gray)
plt.pyplot.subplot(1,2,2)
plt.pyplot.imshow(rwarped,cmap=plt.cm.gray)
plt.pyplot.axis([0,np.max([warped.shape[1],rwarped.shape[1]]),np.max([warped.shape[0],rwarped.shape[0]]),0])
plt.pyplot.axis('off')
plt.pyplot.title('Resize')
"""
rrbw=morphology.closing(rwarped,morphology.square(1)) #闭运算 
plt.pyplot.figure()
plt.pyplot.imshow(rrbw,cmap=plt.cm.gray)

"""
查找边界连通区域
"""
psi=myim.LianTong(rrbw,5,5)

#plt.pyplot.figure()
#plt.pyplot.imshow(psi,cmap=plt.cm.gray)

mypic=((psi==0)|rrbw)
plt.pyplot.figure()
plt.pyplot.imshow(mypic,cmap=plt.cm.gray)






