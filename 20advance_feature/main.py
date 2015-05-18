#!/usr/bin/env python
# coding=utf-8

'''
    切片，可以省去循环
'''
L = range(100)
print L[::10]
print L[::-1]


'''
    迭代
'''
for ch in 'ABC':
    print ch

from collections import Iterable
print isinstance('abc',Iterable)
print isinstance([1,2,3],Iterable)
print isinstance(123,Iterable)

for i,v in enumerate('ABC'):
    print i,v

'''
    generator
'''

def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n = n+1

f = fib(6)
print type(f)


for n in f:
    print n


def odd():
    
    print 'step1'
    a = yield 100  #next暂停处
    print a
    print 'step2' 
    a = yield 200   #send暂停处
    print a
    print 'step3' #send 暂停处
    yield 300

o = odd()
print o.next() 
'''
step1
100
'''
print o.send(1)
'''
1
step2 
200
'''
print o.send(2)
'''
2
step3
300
'''


def odd2():
    print 'step1'
    yield 100
    print 'step2'
    yield 200
    print 'step3'
    yield 300
 
o = odd2()
print type(o)
for n in o:
    print n
