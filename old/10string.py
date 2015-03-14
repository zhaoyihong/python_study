#!/usr/bin/python
#coding=utf-8
#author:zhaoyihong
#email:zhaoyihong@126.com
#date:
'''
字符串常用函数

len()
int() 
ord(s)  chr
find(s[,strart,end])
	rfind
strip(s)
	lstrip
	rstrip
split

'''

 
s1 = 'www.baidu.com'
print len(s1)
li = [1] * 6
print len(li)



i = 1 + int('200')
print i


#ord(char) 返回字符的ascii码
print ord('a')  #97
#print ord('abc') 出错

#chr 数字转换为字符
print chr(97) #a




'''find(sub,[,start [,end]])
返回值是第一次出现的位置

'''
s1 = 'www.baidu.comwww.baidu.com'
print s1.find('baidu')#4


#rfind 从右往左找
print s1.rfind('baidu') #17



''' 
	s.strip() 去掉首位空格
	lstrip() rstrip() 去掉左右字符

	返回拷贝

'''

sp= '  www  '
print sp.strip()


'''
	split([sep [,maxsplit]])

'''

s2 = 'www haha hoho bye'
li = s2.split(' ')
print li #['www', 'haha', 'hoho', 'bye']

s3 = 'aaa...bbb...ccc...d...ccc'
li2 = s3.split('...')
print li2 #['aaa', 'bbb', 'ccc', 'd', 'ccc']



 






	





