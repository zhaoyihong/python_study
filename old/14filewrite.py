#!/usr/bin/python
#coding=utf-8
#author:zhaoyihong
#email:zhaoyihong@126.com
#date:



#格式化写入
fd = open('test.txt','w')
head='%10s%10s%10s\n' % ('id','name','record')
chengji1='%10d%10s%7.2f\n' % (9510425,'zhaoyh',99.0)
chengji2='%10d%10s%7.2f\n' % (9510427,'liupp',95.2)

fd.write(head)
fd.write(chengji1)
fd.write(chengji2)






