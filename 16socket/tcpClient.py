#!/usr/bin/env python
# coding=utf-8

from socket import *

ADDR = 'localhost'
PORT = 21567
HOST = (ADDR,PORT)
BUFSIZE = 1024

while True:
    cliSock = socket(AF_INET,SOCK_STREAM)
    cliSock.connect(HOST)
    data =  raw_input('>')
    if not data:
        break
    cliSock.send('%s\r\n' % data)
    data = cliSock.recv(BUFSIZE)
    if not data:
        break
    print data.strip()
    cliSock.close()
