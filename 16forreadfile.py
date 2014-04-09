#!/usr/bin/python
#coding=utf-8
#author:zhaoyihong
#email:zhaoyihong@126.com
#date:

#使用for读取文件
fr = open('test.txt','r')
for line in fr :
	line = line.rstrip('\n')
	print line
else :
	print 'out of file'
fr.close()


'''
for 使用迭代器来遍历聚合对象:字符串 元组 列表 文件
其中for迭代文件时,每次取出一行
迭代器 iterator
si = iter(s)
si.next()获取下一个对象

'''
s = 'www.baidu.com'

for ch in s:
	print ch

#si = iter(s)






