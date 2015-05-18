#!/usr/bin/env python
# coding=utf-8

def log(func):
    def wrapper(*args,**kw):
        print 'call %s()' % func.__name__
        return func(*args,**kw)
    return wrapper


#now = log(now) = wrapper 
#now(i) = wrapper(i)
@log
def now(i):
    print '2015-05-18,%d' % i

now(100)
print now.__name__ #wrapper


def log2(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print '%s %s' % (text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator
'''
    now2 = log2(text)(now2) = decorator(now2) = wrapper
'''
@log2('hello world')
def now2():
    print '2015-05-18'

now2()
print now2.__name__ #wrapper



