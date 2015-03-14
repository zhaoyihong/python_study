#!/usr/bin/env python
# coding=utf-8

a={1,2,3,4}
b={3,4,5,6}
print a|b  #并集
print a&b  #交集
print a-b  #差集
print b-a
print a ^ b #对称差集 (并集 - 交集)
print a ^ b == (a-b) | (b-a)
print a ^b  == (a|b) - (a&b)
