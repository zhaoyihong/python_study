#!/usr/bin/env python
# coding=utf-8


'''

##习题5：

已知元组:a = (1,4,5,6,7)
1 判断元素4是否在元组里
2 把元素5修改成8

'''
#1
a = (1,4,5,6,7)
print 4 in a

#2 
b = list(a)
b[2] = 8
a = tuple(b)
print a

