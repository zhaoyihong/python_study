#!/usr/bin/python
#coding=utf-8
#author:zhaoyihong
#email:zhaoyihong@126.com
#date:

# readline() 当读取到文件尾时,返回''空串


fr = open('test.txt','r')
line = fr.readline()
while line != '':
	print line.rstrip('\n')
	line = fr.readline()
else :
	print 'out of test.txt'

fr.close()






