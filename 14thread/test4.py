#!/usr/bin/env python
# coding=utf-8

def func():
    x = yield 1 #加入可迭代返回值中
    print x
    x = yield 2 #加入可迭代返回值中
    print x
    yield

m = func()
print m.next()
print m.send("hello")
print m.send("world")

