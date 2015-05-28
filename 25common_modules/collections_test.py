#!/usr/bin/env python
# coding=utf-8

'''
    有名元组，适合较小的数据结构
'''

from collections import namedtuple

Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print p.x,p.y


'''
    deque 适合双端插入和删除
'''
from collections import deque
q = deque(['a','b','c'])
q.append('d')
q.appendleft('x')
print q
print q.popleft()
print q.pop()
print q

'''
    defaultdict
    有默认值的dict
'''
from collections import defaultdict
dd = defaultdict(lambda:'N/A')
dd['key1'] = 'abc'
print dd['key1']
print dd['key2']

'''
    OrderedDict
    按照插入顺序排序的数组
'''
from collections import OrderedDict 
odict = OrderedDict([('d',1),('a',2),('b',3)])
print odict.keys()

'''
    Counter
    计数器
'''
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print c

c = Counter('programming')
print c
print c.most_common(1)

