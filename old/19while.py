#!/usr/bin/env python
# coding=utf-8

num = 1234
sum = 0
while num > 0:
    sum = sum + num %10;
    num = num / 100;
print sum
