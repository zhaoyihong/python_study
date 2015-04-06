#!/usr/bin/env python
# coding=utf-8

import socket

'''
    socket 客户端
'''

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',8225))

s.sendall("hello,world")

buf = s.recv(1024)

s.close()

print "received:",repr(buf)


