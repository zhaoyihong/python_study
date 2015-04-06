#!/usr/bin/env python
# coding=utf-8

import threading


num = 0

def test():
    global num
    num += 1
    print num

ts = []

for i in xrange(0,15):
    th = threading.Thread(target=test)
    th.start()
    ts.append(th)
    

for i in ts:
    i.join()

print "end"
