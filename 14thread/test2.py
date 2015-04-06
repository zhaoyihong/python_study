#!/usr/bin/env python
# coding=utf-8

import time
import threading

def funa():
    print "begin a"
    time.sleep(2)
    print "end a"

def funb():
    print "begin b"
    time.sleep(2)
    print "end b"

beg = time.time()

funa()
funb()

print "use time : %f senconds." %  (time.time()-beg)

beg = time.time()

ta = threading.Thread(target=funa)
tb = threading.Thread(target=funb)

ta.start()
tb.start()

ta.join()
tb.join()

print "use time : %f senconds." %  (time.time()-beg)




