#!/usr/bin/env python
# coding=utf-8

class Rabbit(object):
    
    '''
        静态成员
    '''
    cnt = 0

    def __init__(self,name):
        self.__name = name
        Rabbit.cnt = Rabbit.cnt+1
    '''
        静态方法
    '''
    @staticmethod
    def sget_cnt():
        return Rabbit.cnt

    '''
        类方法
    '''
    @classmethod
    def get_cnt(cls):
        print cls.__name__
        return cls.cnt

    '''
        类实例方法
    '''
    def get_name(self):
        return self.__name
    


print Rabbit.sget_cnt()

print Rabbit.get_cnt()

s = Rabbit('xiaotuzi')
print s.get_name()
print s.get_cnt()
