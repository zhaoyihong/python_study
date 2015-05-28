#!/usr/bin/env python
# coding=utf-8

import struct



#转化为二进制
#I是整数，将>是网络字节序
m = struct.pack('>I',10240099)
print m

#读取bmp文件的前30个字节
s = '\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
#I是整型，H是二字节整型
print  struct.unpack('<ccIIIIIIHH',s)
