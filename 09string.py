#!/usr/bin/python
#coding=utf-8
#author:zhaoyihong
#email:zhaoyihong@126.com
#date:2014-04-1



if __name__ == "__main__":
	str1 = "helloworld"
	print str1[0]  #
	print type(str1[0]) #<type,'str'>
	print type(str1)   #<type,'str'>

	s2 = 'aaa\nbbbb'
	print s2
	
	#字符串前面加r时,斜杠不做转义字符 
	# 例如windows下打开文件 open('c:\templt\text.t','a+') 路径会被转义.(windows路径分隔符是反斜杠,好不方便)
	s3 = r'aaaa\nbbb'
	print s3

	#表明是unicode编码字符串,有什么区别不懂
	s4 = u'aaa\nbbb'
	print s4

	#格式化字符串
	s5 = 'your age is %d,sex %s,record %.1f' % (20,'male',99.2)
	print s5
	
	
	'''
		字符串基本操作
		连接  
		重复 
		索引
		切片
		for循环遍历

	'''

	# 用+将字符串连接起来
	s1 = 'www.baidu'
	s2 = '.com'
	print s1,s2  #www.baidu .com
	print s1+s2 #www.baidu.com
	
	#整形跟字符串的连接 . 注意+两边都必须是字符串
	s1 = 'print'
	i = 10
	s2 = 'times'
	s3 = s1 + ' ' + str(i) + ' ' + s2; #用str()转换为字符串
	print  s3
	

	#重复
	li1 = [1] * 5
	print li1 #[1,1,1,1,1]
	s1 = 'abc'
	s2 = s1*5
	print s2 #abcabcabcabcabc	

	#索引 index
	ch = s2[2]
	print ch

	'''
	切片 [start:end+1]

	'''

	#切片 slice 最后一个不包含
	s3 = s2[0:3]
	print s3	

	#地点默认是0
	s4 = s2[:3]
	print s4

	#终点默认是最后一位后一位
	s5 = s2[3:]
	print s5

	
	s6 = s2[:]	
	print s6

	s7 = s2[-4:-1]
	print s7 #cab

	'''
	切片的步长
	[start:end+1:step]

	'''	
	#空的 ,因为步长默认是1
	s8 = s2[-1:-4]
	print s8 #space
	
	s9 = s2[-1:-4:-1]
	print s9 #abc
	

	#打印逆序的字符串 
	s10 = 'www.baidu.com'
	print s10[::-1]
	

	'''
	for循环
	遍历字符串

	'''
	for ch in s10:
		print ch,


