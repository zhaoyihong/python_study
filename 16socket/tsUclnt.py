#!/usr/bin/env python
# coding=utf-8

from socket import *

HOST = 'localhost'
PORT = 21567
ADDR = (HOST,PORT)
BUFSIZE = 1024

cliSock = socket(AF_INET,SOCK_DGRAM)

while True:
    data = raw_input('>')
    if not data:
        break
    cliSock.sendto(data,ADDR)
    data,addr = cliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print data

cliSock.close()

