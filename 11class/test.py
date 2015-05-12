#!/usr/bin/env python
# coding=utf-8

'''
    静态属性
    相当于c++中的static成员变量
'''

class C:
    a = 100

print C.a

C.a = 200
print C.a

c1 = C()
print c1.a



'''
    方法：
    python中的方法必须和实例绑定，不能直接调用类中的方法
    
    c++中的静态方法在python中不存在了
'''

class D:
    def welcome(self):
        print "hello world"

d = D()
d.welcome()

'''
    构造器 __init__

    析构器 __del__
'''


