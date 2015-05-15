#!/usr/bin/env python
# coding=utf-8
import thread
from time import ctime,sleep

sleeptime = [4,2]

def loop(nloop,nsec,lock):
    print 'start loop %d at %s' % (nloop,ctime())
    sleep(nsec)
    print 'end loop %d at %s' % (nloop,ctime())
    lock.release() #解锁


def main():
    print 'start main at %s' % ctime()
    locks = [] #存放锁的容器
    nloops = range(len(sleeptime)) #存放函数序号

    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire() #加锁
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop,(i,sleeptime[i],locks[i]))

    #阻塞主线程直到两个锁都被释放 ，locked判断锁是否是锁上状态
    for i in nloops:
        while locks[i].locked() : pass
   
main()

