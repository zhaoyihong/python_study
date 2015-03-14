#!/usr/bin/python
#coding=utf-8
#author:zhaoyihong
#email:zhaoyihong@126.com
#date:2014-04-02
'''
继续写string的常用函数

isalunm() #判断是否是数字和字符构成

'''

s='abcdefg12345'
print s.isalnum() # true

s1='abd_23'
print s1.isalnum() #false


'''
isalpha()
isdigit()

'''

s3 = 'abcde'
s4 = '012345'
print s3.isalpha()
print s4.isdigit()


s = raw_input("please input your passwd\n")
if s.isdigit():
	print "your passwd is too simple"
elif s.isalpha():
	print 'your passwd is too simple'
elif s.isalnum():
	print 'your passwd is so strong'
else :
	print 'your passwd is very strong'


'''
	islower()  是小写吗
	isupper() 是大写吗
'''

s5 = 'abcde'
print s5.islower() #ture

s6 = 'BAASS'
print s6.isupper()#true

s7 = 'BASabc'
print s7.islower()#false
print s7.isupper()#false

s8 = '123abc'
print s8.islower() #true

s9 = '123ABC'
print s9.isupper()#true



'''
	isspace()

	全部由空格组成吗?
'''
s10 = '    '
print s10.isspace() #true  


'''
	upper() 转换为大写
	lower() 转换为小写

'''
print 'abcABC'.upper() #ABCABC
print 'abcABC'.lower() #abcabc


'''
	startswith()
	endswith()

'''
print 'www.baidu.com'.startswith('www') #true
print 'www.baidu,com'.endswith('com')   #true


'''
查找
	find('')
	rfind('')
	
'''
print 'www.baidu.comwww.baidu.com'.find('baidu')#4
print 'www.baidu.comwww.baidu.com'.rfind('baidu')#17


'''
	replace(old,new)

字符串不可改变,返回的是拷贝
'''
print 'www.baidu.com,www.baidu.com'.replace('baidu','baidu'.upper())
#www.BAIDU.com,www.BAIDU.com


'''
替换相当于这样
'''
s = 'jeapedu'
s1 = s[:3]
s2 = s[-3:]
print s1 + 'P' + s2 #jeaPedu









