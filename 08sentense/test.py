#!/usr/bin/env python
# coding=utf-8


a=1
b=2
if a+b == 3:
    print "a+b==3"
else:
    print "a+b!=3"


x=a+b
if x:
    print "a+b==3"
else:
    print "a+b!=3"
   
x = 100

if x == 10:
    print "you guess it!"
elif x > 10:
    print "x is too large "
else:
    print "x is too small"

a=-10
x = a if a>0 else -a
print x

a=100
b=200
c = a-b if a>b else b-a
print c


