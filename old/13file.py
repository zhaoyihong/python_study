#!/usr/bin/python
#coding=utf-8
#author:zhaoyihong
#email:zhaoyihong@126.com
#date:2014-04-03

'''
打开文件 : 建立程序与文件的联系
file_obj = open(filename,mode)
	win下注意斜杠转义
	原字符串 r'c:\temp\text'
	转义字符串   'c:\\temp\\text'
	mode
	r 读
	w 写
	a 追加
	+
	b

读写文件:
	read  全部读回来 或者读指定个字符-> string
	readline 读一行 ->string
	readlines 读多行 -> a list of strings

	write   
	  write(str) -> None.  Write string str to file.
    Note that due to buffering, flush() or close() may be needed before
    the file on disk reflects the data written.

	writelines

关闭文件

	close()
'''




fileobj = open('test.txt','r+')
'''
   read([size]) -> read at most size bytes, returned as a string.
   如果不写size,则读取到文件结束
'''
s = fileobj.read()
print s,
'''
aaa
bbb
ccc

'''


'''
	readline([size]) 读取一行,并保留换行符 
	如果不写size,一次读一行,如果写size,返回这行中前size个元素

'''

fileobj.seek(0)
s = fileobj.readline()
print s,  #aaa\n
#去掉\n
s = s.rstrip('\n')
print s



s = fileobj.readline(2)
print s  ##bb


fileobj.seek(0)
print fileobj.readlines()
#['aaa\n', 'bbb\n', 'ccc\n']


fileobj.close()






