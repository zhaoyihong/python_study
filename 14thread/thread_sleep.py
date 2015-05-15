#!/usr/bin/env python
# coding=utf-8

'''
    thread模块使用
    thread模块对不同步的支持太少，推荐使用更高级的threading
'''

import thread
from time import sleep,ctime

def loop0():
    print 'strat loop 0 at %s' % ctime()
    sleep(4)
    print 'end loop 0 at %s' % ctime()

def loop1():
    print 'strat loop 1 at %s' % ctime()
    sleep(4)
    print 'end loop 1 at %s' % ctime()

def main():
    print 'start main at %s' % ctime()
    thread.start_new_thread(loop0,())
    thread.start_new_thread(loop1,())
    sleep(6)    
    print 'end main at %s' % ctime()

if __name__ == '__main__':
    main()
