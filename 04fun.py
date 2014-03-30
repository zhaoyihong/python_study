#!/usr/bin/python
#coding=utf-8
'''
python 函数
1 系统提供内部函数库
2 第三方提供函数库
3 自定义函数

'''

#1字符串函数; 通过help(str)查看信息
s1 = 'jeapedu'
print s1.islower() #判断是否都是小写
print s1.isspace() #判断是是空格
print s1.isdigit() #判断是否是数字
s2 = '111abababab222'
s3 = s2.replace('ab','AB')
print s3  #111ABABABAB222

#2 数学函数 ; 通过 import math; help(math)查看信息
import math
val = math.sin(math.pi/6) #sin6/pi
print math.pow(2,3)
print math.fabs(-1)

#3 系统库  os
import os
current_dir =os.getcwd()
print current_dir
print os.listdir(current_dir)


#网络编程 socket
import socket
baiduip = socket.gethostbyname('www.baidu.com')
print baiduip




