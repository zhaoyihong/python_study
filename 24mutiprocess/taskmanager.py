#!/usr/bin/env python
# coding=utf-8

import random,time,Queue
from multiprocessing.managers import BaseManager

task_queue = Queue.Queue()
result_queue = Queue.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue',callable=lambda:result_queue)

manager = QueueManager(address=('',5002),authkey='abc')
manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    n = random.randint(0,10000)
    print 'put task %d...' % n
    task.put(n)

print 'Try get results...'

for i in range(10):
    n = result.get(timeout=10)
    print 'Result %s' % n

manager.shutdown()
    
