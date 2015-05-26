#!/usr/bin/env python
# coding=utf-8

'''
    要使用property装饰器必须要是新式类
'''
class Stu(object):
    def __init__(self):
        self.__age = 100
    
    @property
    def age(self):
        print 'getter'
        return self.__age
    
    
    @age.setter
    def age(self,value):
        print 'setter'
        self.__age = value

    @age.deleter
    def age(self):
        print 'deleter'
        del self.__age

s = Stu()
s.age = 1000 #setter
print s.age #getter
del s.age #deleter
