#!/usr/bin/python
#coding=utf-8
#author:zhaoyihong
#email:zhaoyihong@126.com
#date:2014-03-31

'''
for target in sequuence:
(TAB)statements


序列类型:
字符串
列表
元组
文件

'''


if __name__ == "__main__":
	#遍历字符串,每次取一个字符
	i=0
	s1 = 'hellworld'
	for char in s1:
		i = i + 1
		print format(i,'2d'),char 
	else:
		print 'out for'


	#遍历列表
	li1 = [1,3,4,5,7,'x',12.5]
	for var in li1:
		print var
	else:
		print 'out li1'		

	
	li2 = list(s1) #字符串转换成列表
	print li2
	for var in li2:
		print var
	else:
		print 'out li2'	
	

	
	for var in 'hello world':
		print var
	else:
		print 'out hello world'		

	
	for var in [1,2,3,4,5]:
		print var
	else:
		print 'out',[1,2,3,4,5]		


	for var in range(1,100,5):
		print var
	else:
		print 'out range(1,100,5)'

	tupe = (1,2,3,4,5)
	for var in tupe:
		print var
	else:
		print 'out of tupe'



	#遍历文件
	
	for n in open('a.txt','r'):
		print n
	else:
		print 'out a.txt'	
	#n是指每行

	li3 = open('a.txt','r').readlines()
	fb = open('b.txt','a+')
	for line in li3:
		print line,
		fb.write(line) #写入到txt中
	else:
		print 'out li3'	
	print len(li3)

	print open('a.txt','r').readline(),

	'''
	文件操作中 readlines()返回列表 ,每个元素是每一行,包含其中的newline符号
	readline()读取一行,返回字符串,也包含newline

	'''

