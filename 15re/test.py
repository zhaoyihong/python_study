#!/usr/bin/env python
# coding=utf-8

import re 

s = "111 222 333 444 555"
for i in re.finditer('\d+',s):
    print i.group(),i.span()


