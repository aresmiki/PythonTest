""" 


 """

import numpy as np 
import pandas as pd
import matplotlib as plt
import PIL.Image as imr 

im1=plt.image.imread('G:/4C/Python/zz.png')
plt.pyplot.figure('image1')
plt.pyplot.imshow(im1)
plt.pyplot.show()

im2=imr.open('G:/4C/03ganhao/015801242_K1597131_0001_5_03.jpg')
Tim2=plt.pyplot.imread('G:/4C/03ganhao/015801242_K1597131_0001_5_03.jpg')
#im3=np.asarray(im2)

plt.pyplot.figure('imageT')
plt.pyplot.imshow(Tim2)
plt.pyplot.show()

print(im2.size)
print(im2.mode)
print(im2.format)
print(im2.getpixel((0,0)))

plt.pyplot.figure('image2')


im3=im2.convert('RGB')

plt.pyplot.imshow(im2)
plt.pyplot.show()
imr.Image.getpixel()



import collections as coll
a=range(10)
print(isinstance(a,coll.Iterator))
print(isinstance(a,coll.Iterable))
print(isinstance((x for x in range(10)),coll.Iterator))




im=imr.Image.open('G:/4C/03ganhao/015801242_K1597131_0001_5_03.jpg')
imr.Image.Image.show(im)
print(im.mode)
imc1=im.convert('RGB')

imc2=np.array(imc1)

plt.pyplot.figure('imc1')
plt.pyplot.imshow(imc2)
plt.pyplot.axis('off')
plt.pyplot.show()
