#!/usr/bin/env python
# coding=utf-8

'''
列表推导 和 字典推导
[ func(x) for x in xs if ... ]
[ func(x) for x in xs ]

'''

nums=[1,2,3,4,5,6];


#获取偶数
evens=[i for i in nums if i%2 == 0]
print evens

#每个元素乘以2
x2=[i*2 for i in nums ]
print x2

#推导出一个字典
dicts={ i : i*2  for i in nums }
print dicts




