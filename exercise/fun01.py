#!/usr/bin/env python
# coding=utf-8

'''
1.定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值。
'''
def max_and_min(*ints):
    '''
        @ints 任意多的整型参数
        返回最大与最小值的元组,找不到返回None
    '''
    if 0 == len(ints):
        return None
    
    return (min(ints),max(ints))
   
assert max_and_min(2,30,100,0) == (0,100)
assert None == max_and_min()

'''
    2.定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。
'''
def longest_str(*strs):
    '''
    @strs:任意多的字符串
    返回最长的字符串
    '''
    if 0 == len(strs):
        return None

    maxlen = len(strs[0])
    maxindex = 0
    index = 0
    for s  in strs:
        if len(s) > maxlen:
            maxlen = len(s)
            maxindex = index
        index += 1

    return strs[maxindex]

assert None == longest_str()
assert "helloworld" == longest_str("abc","long","helloworld","haha")


'''
3.定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档。

'''
def get_doc(module):
    pass

'''
4.定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。
'''
def get_text(f):
    '''
    @f 文件路径
    返回文件内容，若文件不存在返回None
    '''
    import os 
    if not os.path.exists(f):
        return "文件不存在"

    try:
        file = open(f,"r")
    except IOError:
        return '文件无法读取'
    except:
        return '其他错误'
    else:
        content = file.read()
        file.close()
        return content

print get_text("/home/yihong/a.txt")


'''
folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表。提示（可以了解python的glob模块）
'''
def get_files(dirpath):
    '''
    @dirpath 文件夹路径
    返回 文件夹下的文件
    '''
    import os 
    if not os.path.isdir(dirpath):
        return "文件夹路径不正确"

    return os.listdir(dirpath)

print get_files("/home/yihong")
