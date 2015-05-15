#!/usr/bin/env python
# coding=utf-8
import threading
from time import ctime,sleep


class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self): #重写run函数
        apply(self.func,self.args)

def loop(nloop,nsec):
    print 'start loop %d at %s' % (nloop,ctime())
    sleep(nsec)
    print 'end loop %d at %s' % (nloop,ctime())

def main():
    sleeptime = [4,2]
    print 'starting at %s' % ctime()
    threads = []
    nloops = range(len(sleeptime))
    
    for i in nloops:
        t = MyThread(loop,(i,sleeptime[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()
    
    print 'end at %s' % ctime()


main()
