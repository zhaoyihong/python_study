#!/usr/bin/env python
# coding=utf-8

from Queue import Queue
from time import sleep
from random import randint 
import threading


def writeQ(queue):
    print 'producting object from Q...'
    queue.put('x',1)
    print 'size now %d' % queue.qsize()

def readQ(queue):
    queue.get(1)
    print 'consuming object from Q...'
    print 'size now %d' % queue.qsize()

def writer(queue,loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1,3))

def reader(queue,loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2,5))

funcs = [writer,reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2,5) #生产/消费次数
    q = Queue(32)
    threads = []

    for i in nfuncs:
        t = threading.Thread(target=funcs[i],args=(q,nloops))
        threads.append(t)

    for th in threads:
        th.start()
    
    print 'all done'

if __name__ == "__main__":
    main()
