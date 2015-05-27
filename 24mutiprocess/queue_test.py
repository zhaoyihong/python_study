#!/usr/bin/env python
# coding=utf-8

from multiprocessing import Process,Queue
import os,time,random

def write(q):
    for value in range(10):
        print 'Put %d to queue...' % value
        q.put(value)
        time.sleep(random.random())

def read(q):
    while True:
        value = q.get(True)
        print 'Get %d from queue' % value

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()

    pr.terminate()

