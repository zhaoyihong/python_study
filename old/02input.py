#!/usr/bin/python
# coding=utf-8

#概要 raw_input读取输入,返回值是字符串
#若想要其他两种类型 用转换int() float()


#读到回车结束,字符串不包含回车 ,raw_input返回值是字符串
str1 = raw_input("please input a string:\n")
print type(str1) #<type 'str'>	
print str1

#希望读取整数 使用int()强制转换成整形
age = int(raw_input("please intput your age\n"))
print type(age)
print age
age = 1 + age


#希望读取浮点型
weight = float(raw_input("please int put your weight:\n"))
print type(weight)

