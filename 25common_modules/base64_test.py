#!/usr/bin/env python
# coding=utf-8
import base64

#url = 'i\xb7\x1d\xfb\xef\xff'
url = 'www.baidu.com'

m = base64.b64encode(url)
print m
print base64.b64decode(m)

# urlsafencode 中不会出现+和/,被转化为-和_

n = base64.urlsafe_b64encode(url)
print n
print base64.urlsafe_b64decode(n)

# =在url和cookie中有歧义，程序员会将后面的=去掉，再进行传输
n = n.rstrip('=')
print n
#还原时要进行检查，看编码是否是4的倍数，如果不是用=补齐
def safe_deconde(n):
    return base64.urlsafe_b64decode(n+('='*(4-len(n)%4)))
print safe_deconde(n)



