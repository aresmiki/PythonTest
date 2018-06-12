# learing 2
# import sys
# sys.path.append('/Users/heliu/projiect/Python')

# The method 1 of import py file
# import myfuction as foo
# foo.fun(8)

# The method 2 of import py file
# from myfuction import fun as foo
# c=foo(8)
# print(c)

# The method 3 of import py file
#import sys,os    #对于重新装的软件，在导入函数模块时，需要将os导入一次，将文件路径更改正确，否则会报import错误（对于py文件而言）
import myfuction as foo
print(foo.fun(3))
print(foo.fun2(3,2,1))
foo.fun3()

