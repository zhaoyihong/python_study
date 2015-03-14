#!/usr/bin/python
#coding=utf-8
'''
概要:
1 变量指向地址 而不是指向内容
  可以改变变量的地址,而不能改变其中内容
  id()    返回变量地址
  str()   转换为字符串

2 python 变量数据类型不需要指定
	type() 返回数据类型
'''

#1 赋值改变变量指向地址
x = 12
y = 13
print x,y
#id()返回对象的地址
print 'id(x)'+str(id(x))
print 'id(y)'+str(id(y))
x=14
print 'after modifyed id(x) become:'+str(id(x))
#我们发现x赋值前后的id变了 说明x赋值后指向了别的内存


#2 python 变量 赋予什么类型就是什么类型
name = 'zhaoyh'
print type(name)
age = 20
print type(age)

#3 和c语言的区别
'''
	c语言中int x = 10;
	变量一次分配,始终指向那块内存 &x是不变的
	x=20; 改变了&x地址中的值

	python 不能改变内存中的值,只能改变变量指向
'''
x = 10
y = 20
print x,id(x)
print y,id(y)

#x y的指向的地址变成一样了
x = y
print x,id(x)
print y,id(y)

'''
这时x又变成10了,这时地址和前一个是一样的; y也被赋值,值和以前一样.
这时发现 x指向的地址和上上轮一样,y的地址和上轮一样,这说明python会重复使用常量

'''
x = 10
y = 20
print x,id(x)
print y,id(y)











