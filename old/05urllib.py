#!/usr/bin/python
#coding=utf-8
#author:zhaoyihong
#email:zhaoyihong@126.com
#date:2014-03-30

#引入第三方库 urllib
import urllib

if __name__ == "__main__":
	url = 'http://www.163.com'
	content = urllib.urlopen(url).read() #获取url的页面的内容
	open('163.html','w').write(content) #将content写入到文件中
	
	
		














