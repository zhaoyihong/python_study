#!/usr/bin/env python
# coding=utf-8

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print 'call %s' % func.__name__
        return func()
    return wrapper

@log
def now():
    print '2015-05-18'

now()
print now.__name__


def log2(text):
    def decortator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print '%s %s' % (text,func.__name__)
            return func()
        return wrapper
    return decortator

@log2('excute')
def now2():
    print '2015-05-18'

now2()
print now2.__name__
