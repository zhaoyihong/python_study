#!/usr/bin/env python
# coding=utf-8
import hashlib

'''
    md5 和 sha1 都是常用的 摘要算法
    主要是为了防止篡改
'''

md5 = hashlib.md5()
md5.update('how to use md5 in python?')
print md5.hexdigest()

#如果数据量大，可以多次放入
md5 = hashlib.md5()
md5.update('how to use ')
md5.update('md5 in python?')
print md5.hexdigest()

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in python?')
print sha1.hexdigest()

def calc_md5(passwd):
    md5 = hashlib.md5()
    md5.update(passwd)
    return md5.hexdigest()

print calc_md5('12345')
print calc_md5('woshihanmeimei')

db = {
    'lilei':'827ccb0eea8a706c4c34a16891f84e7b',
    'hanmeimei':'dd55b43a8b7b4339115846ee024d9e2b'
    }


def login():
    global db
    user = raw_input('please input your username.')
    if user not in db:
        print 'user not exist!'
        return False
    try_cnt = 3
    for i in range(try_cnt):
        passwd = raw_input('please input your passwd.')
        md5 = hashlib.md5()
        md5.update(passwd)
        if db[user] == md5.hexdigest():
            print 'success login'
            return True
        else:
            print 'login failed,please try agein'

    return False

login()
