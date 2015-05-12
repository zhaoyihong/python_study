#!/usr/bin/env python
# coding=utf-8

from socket import *

from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print 'waiting for connetcion ...'
    tcpCliSock,addr = tcpSerSock.accept()
    print '... connet from :',addr 

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        msg = '[%s] %s' % (ctime(),data)
        print msg
        tcpCliSock.send(msg)
    tcpCliSock.close()

tcpSerSock.close()
