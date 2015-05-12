#!/usr/bin/env python
# coding=utf-8

from socket import *
from time import ctime

ADDR=''
PORT=21567
HOST=(ADDR,PORT)
BUFSIZE = 1024

serSock = socket(AF_INET,SOCK_DGRAM)
serSock.bind(HOST)

while True:
    print 'waiting for message...'
    data,addr = serSock.recvfrom(BUFSIZE)
    print '[%s] %s:%s' % (ctime(),addr,data)
    serSock.sendto('[%s] %s' % (ctime(),data),addr)

serSock.close()



