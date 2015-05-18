#!/usr/bin/env python
# coding=utf-8

'''
    未绑定的成员变量是静态的
'''

class C:
    foo = 100
    
    @staticmethod
    def say():
        print "foo=%d" % C.foo


'''
    调用静态成员内和静态方法
'''
print C.foo #100
C.foo = 200
print C.foo #00
C.say() #foo=200

'''
    不要用实例来调用静态成员
'''
f = C()
f.foo = 1000
print f.foo #1000
print C.foo #200




