#!/usr/bin/env python
# coding=utf-8


'''
    高阶函数
'''
def add(x,y,func):
    return func(x)+func(y)

print add(-1,-2,abs)

'''
    map/reduce
'''
def f(x):
    return x*x

print map(f,range(10))
print map(str,range(10))


def add2(x,y):
    return x*10 + y
    
print reduce(add2,range(0,10))

def char2num(s):
    return ord(s) - ord('0')

def char2int(s):
    def fn(x,y):
        return 10*x+y
    def char2num(s):
        return ord(s) - ord('0')
    return reduce(fn,map(char2num,s))

print char2int('012345')

'''
    filter
'''

def is_odd(n):
    return n%2 == 1
print filter(is_odd,range(10))


'''
    sorted
'''
print sorted([36,5,12,2,9])

def reverse_cmp(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0

print sorted([36,5,12,2,9],reverse_cmp)


s  = ['bob','about','Credict','Zoo']
print sorted(s)

def igcase_cmp(x,y):
    x1 = x.lower()
    y1 = y.lower()
    return cmp(x1,y1)

print sorted(s,igcase_cmp)



