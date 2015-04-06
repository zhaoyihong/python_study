#!/usr/bin/env python
# coding=utf-8

import bs4
import urllib

content = urllib.urlopen("http://money.163.com/special/pinglun/").read()
assert None != content,"网页抓取失败"
bs4_obj = bs4.BeautifulSoup(content)








