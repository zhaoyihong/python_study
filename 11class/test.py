#!/usr/bin/env python
# coding=utf-8


class test(object):

    #这是一个属性
    a = 100
   
    #构造函数
    def __init__(self,var):
        self.var = var

    #析构函数
    def __def__(self):
        pass

    #普通函数
    def get(self):
        return self.var

    def getA(self):
        return self.a

t = test("hello world")
print t.get()
print t.getA()
print t.a


class Base(object):
    def __init__(self,name):
        self.name = name

class b(Base):
    def get_name(self):
        return self.name


new_class = b('lilei')
print new_class.get_name()


class girl(object):
    '''
       定义一个女孩类
    '''
    gender = 0

    def __init__(self,name):
        self.name = name
    

class boy(object):
    '''
        定义一个男孩
    '''
    gender = 1

    def __init__(self,name):
        self.name = name


class love():
    '''
        恋爱的base类
    '''
    def __init__(self,first,second):
        self.first_name,self.second_name = first.name,second.name

    def meet(self):
        return "%s 和 %s 相遇了。" % (self.first_name,self.second_name)

    def marry(self):
        return "%s 和 %s 结婚了。" % (self.first_name,self.second_name)


class normal_love(love):
    '''
        男女的恋爱
    '''
    def __init__(self,first,second):
        if 1 != first.gender + second.gender:
            print "normal_love.__init__: 参数输入错误"
        else:
            love.__init__(self,first,second)


class gay_love(love):
    '''
        男男的恋爱
    '''
    def __init__(self,first,second):
        if 2 != first.gender + second.gender:
            print "gay_love.__init__: 参数输入错误"
        else:
            love.__init__(self,first,second)


class less_love(love):
    '''
        女女的恋爱
    '''
    def __init__(self,first,second):
        if 0 != first.gender + second.gender:
            print "less_love.__init__: 参数输入错误"
        else:
            love.__init__(self,first,second)


lilei = boy("lilei")
meimei = girl("hanmeimei")
xiaogang = boy("xiaogang")
lucy = girl("lucy")

nl = normal_love(lilei,meimei)
print nl.meet()
print nl.marry()

gl = gay_love(lilei,xiaogang)
print gl.meet()
