#!/usr/bin/env python
# coding=utf-8

import threading

money = 500
mlock = threading.Lock()

def cost1():
    global money
    for i in xrange(0,100):
        mlock.acquire()
        money += 1
        mlock.release()

threads_list = list()

for i in xrange(0,10):
    th = threading.Thread(target=cost1)
    threads_list.append(th)
    th.start()

for th in threads_list:
    th.join()

print "money is %d" %  money



info = [1,2,3,4,55,233]

def printInt(num):
    print num

tlist = list()

for i in xrange(0,len(info)):
    th = threading.Thread(target=printInt,args=[info[i]])
    th.start()
    tlist.append(th)

for th in tlist:
    th.join()

print "end"



import Queue
import urllib
import re


def get_url_title(url):
    file = urllib.urlopen(url)
    content = file.read()
    c = file.code
    re_title = '<title>(.*)</title>'
    title = re.findall(re_title,content)
    if 0 != len(title):
        print url,c,title
    else:
        print url,c, None

urlinfo = ['http://www.renren.com','http://www.baidu.com','http://www.so.com','http://www.sohu.com','http://www.163.com','http://www.sina.com']

queue = Queue.Queue(3)

for url in urlinfo:
    th = threading.Thread(target=get_url_title,args=[url])
    if queue.full():
        wait_th = queue.get()
        wait_th.join()
    queue.put(th)
    th.start()

while not queue.empty():
    th = queue.get()
    th.join()



def fab(num):
    assert num >= 0
    if num == 0 or num == 1:
        yield num
        return 

    x,y = 1,1
    yield x 
    yield y
    while y <= num:
        x,y = y,x+y
        yield y

f = fab(10)
for i in f:
    print i

