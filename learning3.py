#-*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as num

t=num.linspace(0,10,1000)

x=num.sin(1+t)
z=num.cos(1+t**2)

plt.figure
plt.plot(t,x,'-r',linewidth=2)
plt.plot(t,z,'-.b',linewidth=2)
plt.title('Testing line')
plt.xlabel('Time(s)')
plt.ylabel('Volte')
plt.xlim(0,10)
plt.legend(('line1','line2'))
plt.show()




