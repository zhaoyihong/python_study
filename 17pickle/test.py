#!/usr/bin/env python
# coding=utf-8

import pickle

account1 = {"8000":['zhaoyihong',25,9999.9],"80001":['panpan',23,10000]}
account2 = {"9000":['zhaoyihong',25,9999.9],"80001":['panpan',23,10000]}
account3 = {"10000":['zhaoyihong',25,9999.9],"80001":['panpan',23,10000]}

file = open("account_info","wb")

pickle.dump(account1,file)
pickle.dump(account2,file)
pickle.dump(account3,file)

file.close()

file = open("account_info","rb")

try:
    while 1:
        ac = pickle.load(file)
        print ac
except:
    pass



