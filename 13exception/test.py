#!/usr/bin/env python
# coding=utf-8
import sys

a = [1,2,3,4,5]

try:
    print a[5]
except:
    print "try语句块中出错了执行这里"
    #sys.exit(-1)
else:
    print "try语句块中没出错执行这里"
finally:
    print "无论如何都会执行这里，即使中途exit了"


import urllib

sth_url = "http://www.baidu.com"

try:
    d = urllib.open(sth_url)
except IOError:
    print "该url无法打开"
except:
    print "其他错误"
else:
    content = d.read()
    print content
    d.close()

import logging

logger = logging.getLogger() #创建一个logging对象
hdlr = logging.FileHandler('testlog.txt') #创建存放日志的文件句柄
formater = logging.Formatter('%(asctime)s %(levelname)s %(message)s') #设置日志格式
hdlr.setFormatter(formater) #文件绑定格式
logger.addHandler(hdlr)     #logging对象绑定文件句柄
logger.setLevel(logging.NOTSET) #设置日志的最低等级 CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET



try:
    a=3
    assert a==4 , "a!=4"
except:
    exc = sys.exc_info()
    logging.debug(exc[1]) #将异常信息写入logger


with open("a.txt","r") as a:
    print a.read()

class sth(object):

    def __enter__(self):
        print "__enter__"

    def __exit__(self,type,value,traceback):
        print "__exit__"

with sth() as s:
    print "in with"


class MyException(Exception):

    def __init__(self,error,msg):
        self.args = (error,msg)
        self.error = error 
        self.msg = msg

try:
    raise MyException(100,"my exception")
except Exception as e:
    print e.error,",",e.msg


