# learning 1

import numpy as num
import matplotlib.pyplot as pl 

l=[1,'hello',0.4]
t=(1,'hello',0.4)
d={1:'1','hello':0.1,0.4:80}
# test1
if (0.4 in l):
    print("0.4 is in l")
else:
    print("0.4 is not in l")
# test2
if (1 in t):
    print("1 is in t")
else:
    print("1 is not in t")
# test3
if ('abc' in d):
    print("'abc' is in d")
else:
    print("'abc' is not in d")


# test4
b=False
#c=True
c=False
if b:
    print("b is True")
elif c:
    print("c is True")
else:
    print("Both are False")

# test5

m={1:'1','abc':0.1,0.4:80}
for k in m:
    print(k,":",m[k])

# test6

def foo(x):
    return x**2
print(foo(8))

