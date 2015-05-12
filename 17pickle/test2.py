#!/usr/bin/env python
# coding=utf-8

'''
    cPickle 和 pickle一样的用法，但是快很多
'''

import cPickle

account1 = {"8000":['zhaoyihong',25,9999.9],"80001":['panpan',23,10000]}
account2 = {"9000":['zhaoyihong',25,9999.9],"80001":['panpan',23,10000]}
account3 = {"10000":['zhaoyihong',25,9999.9],"80001":['panpan',23,10000]}

file = open("account_info2","wb")

cPickle.dump(account1,file)
cPickle.dump(account2,file)
cPickle.dump(account3,file)

file.close()

file = open("account_info","rb")

while 1:
    try:
        ac = cPickle.load(file)
        print ac
    except EOFError :
        break



