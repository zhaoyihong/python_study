#!/usr/bin/python
#coding=utf-8
#author:zhaoyihong
#email:zhaoyihong@126.com
#date:
import urllib
url='http://www.bubugao.com/gallery-113.html'

def getHtml():
	response = urllib.urlopen(url)
	html=response.read()
	print html

if __name__ == "__main__":
	getHtml()






