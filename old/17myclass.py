#!/usr/bin/env python
# coding=utf-8

class Myclass:
    def __init__(self):
        self.name = "MYCLASS" #添加变量
        print "hello my class!",self.name
    def printName(self):
        print self.name
    def setName(self,name):
        self.name = name

class MyNewClass(Myclass):
    def setAge(self,age):
        self.age = age
    def printAge(self):
        print self.age


myc = Myclass()

myc.setName("apple")
myc.printName()

mync = MyNewClass()
mync.setAge(100)
mync.printAge()
mync.setName("banana")
mync.printName()

