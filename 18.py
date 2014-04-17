#!/usr/bin/python
#coding=utf-8
#author:zhaoyihong
#email:zhaoyihong@126.com
#date:2014-04-10

def count_char(listchars,sep):
	while(sep in listchars):
		#listchars.pop(listchars.index('.'))
		listchars.remove(sep)
#	print listchars
	return len(listchars)
	

if __name__ == "__main__":
	s = 'www.baidu.com'
	li1 = list(s)
	print 'li1 ',li1
	count =  count_char(li1,'.')
	print 'in %s has %d char' % (s,count)

	


