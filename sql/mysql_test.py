#!/usr/bin/env python
# coding=utf-8

import mysql.connector

conn = mysql.connector.connect(user='root',password='123456',database='test',use_unicode=True)
cursor = conn.cursor()
cursor.execute('use test')
cursor.execute('create table if not exists user (id int not null auto_increment primary key ,name varchar(20))')
cursor.execute('insert into user (name) value (%s)',['abc'])

print cursor.rowcount
#提交事务
conn.commit()
cursor.close()


#查询
cursor = conn.cursor()
cursor.execute('select * from user')
values = cursor.fetchall()
print values



