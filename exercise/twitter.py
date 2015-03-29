#!/usr/bin/env python
# coding=utf-8

#将文本存放到list中来，每个元素是一个字典

data_keys = ('bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location', 'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url')

file = open("twitter数据挖掘片段.txt","r")
#file = open("test.txt","r")
info_list = []

for line in file:
    line_list = line.split('","')
    info_dict = { k:line_list[data_keys.index(k)] for k in data_keys }
    info_list.append(info_dict)

file.close()

#file = open("debug.txt",'w')

'''
    1.该文本里，有多少个用户。（要求：输出为一个整数。）

'''
uid_set = set( [ x["uid"] for x in info_list ])
print len(uid_set)


'''
    2.该文本里，每一个用户的名字。 （要求：输出为一个list。）
'''
username_list = list(set([x["username"] for x in info_list]))


'''
    3.该文本里，有多少个2012年11月发布的tweets。 （要求：输出为一个整数。提示：请阅读python的time模块）
'''

time_list = [ x["created_at"] for x in info_list]
list_2012_11 = filter(lambda x:x.startswith('2012-11'),time_list)
print len(list_2012_11)


'''
4.该文本里，有哪几天的数据？ （要求：输出为一个list，例：['2012-03-04','2012-03-05'])
'''
time_days = [ x.split(' ')[0] for x in time_list if len(x)>0 ]
time_days = list(set( time_days ))
time_days.sort()
print "[{0},{1}]".format(time_days[0],time_days[-1])








