#!/usr/bin/env python
# coding=utf-8

from socket import *

BUFSIZE = 1024
ADDR = 'localhost'
PORT = 21567
HOST = (ADDR,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(HOST)

while True:
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print data

tcpCliSock.close()
