#!/usr/bin/env python
# coding=utf-8

import time,sys,Queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

serveraddr = '127.0.0.1'
serverport = 5002

manager = QueueManager(address=(serveraddr,serverport),authkey='abc')

manager.connect()

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    try:
        n = task.get(timeout=1)
        print 'run task %d * %d ' % (n,n)
        r =  '%d * %d = %d' % (n,n,n*n)
        result.put(r)
    except:
        print 'task manager is empty'




