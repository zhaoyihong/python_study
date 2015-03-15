#!/usr/bin/env python
# coding=utf-8

'''
##习题6：


已知集合:setinfo = set('acbdfem')和集合finfo = set('sabcdef')完成下面操作：

1 添加字符串对象'abc'到集合setinfo

2 删除集合setinfo里面的成员m

3 求2个集合的交集和并集

'''

setinfo = set('acbdfem')
finfo = set('sabcdef')
#1 
setinfo.add("abc")
print setinfo
#2
setinfo.remove('m')
print setinfo
#3
print setinfo & finfo
print setinfo | finfo


