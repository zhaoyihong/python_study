#!/usr/bin/env python
# coding=utf-8


from collections import Counter

c=Counter('helloworld')
#打印Counter对象
print c
#打印最多的两个
print c.most_common(2)


