#!/usr/bin/python
#coding=utf-8
#author:zhaoyihong
#email:zhaoyihong@126.com
#date:2014-03-31


'''
自定义函数

def function_name(parameters):
(TAB)statement
(TAB)statement
(TAB)statement


没有返回值类型
参数也不需要类型

'''

#无参数
def test_a():
	print 'hello the cruel world'

#有参数
def test_b(var1,var2):
	print var1,
	print var2

#有返回值		
def test_c(var1,var2):
	return var1+var2


#多返回值
def test_d(var1,var2):
	return var1+var2,var1*var2

#参数默认值 
def test_e(n1,n2=15):
	return n1+n2

if __name__ == "__main__":
	test_a()
	test_a()
	test_b(1,2)
	test_b('helloworld','yes')

	sum = test_c(100,200)
	print sum

	m,n = test_d(100,200)
	print m,n

	#如果只用一个值接收,收到的是元组
	result = test_d(100,200)
	print result  #(300,20000)
	print result[0],result[1]

	print test_e(10)
	print test_e(10,20)

	
