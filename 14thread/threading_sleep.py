#!/usr/bin/env python
# coding=utf-8
import threading
from time import ctime,sleep
sleeptime = [4,2]
def loop(nloop,nsec):
    print 'start loop %d at %s' % (nloop,ctime())
    sleep(nsec)
    print 'end loop %d at %s' % (nloop,ctime())
def main():
    print 'start main at %s' % ctime()
    nloops = range(len(sleeptime)) #存放函数序号
    threads = []
    for i in nloops:
        th = threading.Thread(target=loop,args=(i,sleeptime[i]))
        threads.append(th)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print 'end main at %s' % ctime()
if __name__ == '__main__':
    main()
