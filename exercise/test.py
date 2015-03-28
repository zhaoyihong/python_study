#!/usr/bin/env python
# coding=utf-8

a = "aAsmr3idd4bgs7Dlsf9eAF"
b=a.swapcase() #转化大小写
print b

#list转换为string,不可以用str直接转. 要使用join方法
c = "".join([x for x in a if x.isdigit()])
print c 


d=a.lower()
print dict([(x,d.count(x)) for x in set(d)])


a_list = list(a)
#去重
a_list = list(set(a_list))
a_list.sort(key=a.index)
print "".join(a_list)


alist = list(a)
alist.reverse()
print "".join(alist)


def my_cmp(x,y):
    x1 = x.upper()
    y1 = y.upper()
    if x1 != y1:
        return ord(x1) - ord(y1)
    else:
        return ord(x) - ord(y)

alpha_list = [ x for x in a if x.isalpha() ]
alpha_list.sort(cmp=my_cmp)
print "".join(alpha_list)



'''
    isInclude 判断string中是否含有search中所有的字母
    string 是被搜索的字符串
    search 是搜索的字符串
    包含返回True，不包含返回False
'''
def is_include(string,search):
    str_set = set(string)
    len_bef = len(str_set)
    str_set.update(search)
    len_aft = len(str_set)
    return len_bef == len_aft

a = "aAsmr3idd4bgs7Dlsf9eAF"
b = "boy"
print is_include(a,b)




'''
    isIncludeList 判断string中是否含有search中所有的字母
    string 是被搜索的字符串
    search 是搜索的List
    包含返回True，不包含返回False
'''
def is_includeList(string,search):
    str_set = set(string)
    len_bef = len(str_set)
    search_set = set("".join(search))
    str_set.update(search_set)
    len_aft = len(str_set)
    return len_bef == len_aft

a = "aAsmr3idd4bgs7Dlsf9eAF"
b = ["boy","girl","bird","dirty"]
print is_includeList(a,b)

def most_char(string):
    string_list = [(x,string.count(x)) for x in set(string)]
    string_list.sort(key=lambda x:x[1],reverse=True)
    return string_list[0][0]

a = "aAsmr3idd4bgs7Dlsf9eAF"
print most_char(a)

import os
#os.popen 运行一条系统命令，并将返回一个指向回显的文件对象。
m = os.popen('python -m this').read()
m.replace('\n',' ')
l=m.split()
print [(x,l.count(x)) for x in ('be','this','than')]

size = 102324123499123
kb = size >> 10
mb = kb >> 10
print kb,mb

a = [1,2,3,6,8,9,10,14,17]
print "".join([str(x) for x in a])

