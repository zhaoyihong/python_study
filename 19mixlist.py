#!/usr/bin/python
#coding=utf-8
#author:zhaoyihong
#email:zhaoyihong@126.com
#date:2014-04-18


'''
	将混合型列表写入文件

'''

li = [1,2,3,"hello","world","python",1.1]

fr = open('test.txt','w')

i = 0
while i < len(li):
	item = li[i]
	if( isinstance(item,str) == False ):
		item = str(item)
	fr.write(item+"\n")
	i = i + 1

fr.close()

	 





