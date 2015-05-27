#!/usr/bin/env python
# coding=utf-8
from multiprocessing import Process
import os

def run_proc(name):
    print 'Run child process %s (%s)' % (name,os.getpid())

if __name__ == '__main__':
    print 'Parent process is %s' % os.getpid()
    print 'Process will start'
    p = Process(target=run_proc,args=('test',))
    p.start()
    p.join()
    print 'Process end'



