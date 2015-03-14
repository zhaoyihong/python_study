#!/usr/bin/python
#coding=utf-8
#author:zhaoyihong
#email:zhaoyihong@126.com
#date: 2014-04-02



s = '   12a  34b   232  yed   eff   '
print s.split(' ')
# ['', '', '', '12a', '', '34b', '', '', '232', '', 'yed', '', '', 'eff', '', '', ''] 显然是不行的




s = s.strip()
index = s.find(' ')
while index != -1:
	print s[:index]
	s = s[index:].strip()
	index = s.find(' ')
print s #the last one
		
