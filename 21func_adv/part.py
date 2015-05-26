#!/usr/bin/env python
# coding=utf-8

'''
偏函数
'''

'''
    有时候要调用函数需要2个参数
'''
print int('10010',2) #2进制字符串转整数

import functools
int2 = functools.partial(int,base=2)
print int2('10010')

'''
    partial 接收的3个参数 ，函数，*args, **kw
    上面的base=2 就是 **kw,设置函数的对应的参数
    下面的这个是设置的args，10将被放在max的最左边
'''

max2 = functools.partial(max,10)
print max2(2,3,4,5) #10 


