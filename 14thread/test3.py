#!/usr/bin/env python
# coding=utf-8

'''
    线程中的互斥锁
'''

import threading
mlock = threading.RLock() #锁对象
num=0

def fun():
    global num
    mlock.acquire() #加锁
    num+=1
    mlock.acquire()
    print num
    mlock.release()
    mlock.release()


for i in xrange(0,15):
    th = threading.Thread(target=fun)
    th.start()



