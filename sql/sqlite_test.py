#!/usr/bin/env python
# coding=utf-8
import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('create table if not exists user (id int not null ,name varchar(20))')
cursor.execute('insert into user (id,name) values (1,\'machel\')')
print cursor.rowcount

cursor.close()
conn.commit()

cursor = conn.cursor()
cursor.execute('select * from user')
values = cursor.fetchall()
print values

conn.close()
