#!/usr/bin/env python
# coding=utf-8

from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print 'Run task %s (%s)' % (name,os.getpid())
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print 'task %s run %.2f seconds' % (name,(end-start))

if __name__ == '__main__':
    print 'parent process is %s.' %  os.getpid()
    p = Pool(5) #进程池大小，默认是4
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close() 
    p.join()#要先close再join
    print 'All subprocesses done'

    


