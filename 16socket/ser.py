#!/usr/bin/env python
# coding=utf-8


import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('127.0.0.1',8225))

s.listen(100)

conn,address = s.accept()

while True:
    
    buf = conn.recv(1024)
    
    if not buf : break

    conn.sendall(buf)
    
conn.close()



s.close()

