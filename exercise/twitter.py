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


'''
5.该文本里，在哪个小时发布的数据最多？ （要求：输出一个整数。）
'''
#所有的小时
hours_list = [ x.split(' ')[1].split(':')[0] for x in time_list if len(x)>0 ]
#小时去重
hours_set = set(hours_list)
#统计小时的计数
hours_cnt_dict = { x:hours_list.count(x) for x in hours_set  }
#依据计数进行排序
hours_cnt_list = hours_cnt_dict.items()
hours_cnt_list.sort(key=lambda x:x[1],reverse=True)
print hours_cnt_list[0][0]


'''
6.该文本里，输出在每一天发表tweets最多的用户。（要求：输出一个字典。例如 {
'2012-03-04':'agelin','2012-03-5':'twa'}）
'''

most_users_of_day = {}
day_user_dict = { x:dict() for x in time_days }

for info in info_list:
    day = info["created_at"].split()[0]
    user = info["username"]
    if day_user_dict[day].has_key(user):
        day_user_dict[day][user] += 1
    else:
        day_user_dict[day][user] = 1
    
for day,users in day_user_dict.items():
    user_tupel_list = users.items()
    user_tupel_list.sort(key=lambda x:x[1],reverse=True)
    most_users_of_day[day] = user_tupel_list[0][0]

print most_users_of_day


'''
7. 请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率（要求：输出为一个list [(1,20),(2,30)] 代表1点发了20个tweets，2点发了30个tweets） 
'''
info_20121103_list = filter(lambda x : x["created_at"].startswith("2012-11-03"),info_list)
hours_list = [x["created_at"].split()[1].split(':')[0] for x in  info_20121103_list]
hours_set = set(hours_list)
hour_cnt_list = [ (x,hours_list.count(x)) for x in hours_set ]
hour_cnt_list.sort(key=lambda x:x[0],cmp=lambda x,y:int(x)-int(y))
print hour_cnt_list

'''
8. 统计该文本里，来源的相关信息和次数，比如（输出一个list。例如[('Twitter for Android',1),('TweetList!',1)]

'''
sources_list = [x["source"] for x in info_list ]
sources_set = set(sources_list)
sources_tuple_list = [(x,sources_list.count(x)) for x in sources_set ]
print sources_tuple_list

'''
9. 计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个。(要求，输出一个整数。)

'''
cnt = 0
for info in info_list:
    if info["rt_v_url"].startswith("https://twitter.com/umiushi_no_uta"):
        cnt += 1
print cnt

'''
10. UID为573638104的用户 发了多少个微博 （要求：输出一个整数）
'''

cnt = 0
for info in info_list:
    if info["uid"] == "573638104":
        cnt += 1
print cnt 

'''
11. 定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid。
'''

def most_uid(*kargs):

    if len(kargs) == 0:
        return None

    uid_cnt_dict = { uid:0 for uid in kargs }
    for info in info_list:
        uid = info["uid"]
        if uid_cnt_dict.has_key(uid):
            uid_cnt_dict[uid] += 1
    
    uid_cnt_list = uid_cnt_dict.items()
    uid_cnt_list.sort(reverse=True,key=lambda x:x[1])
    return uid_cnt_list[0][0]

# print  most_uid("573638104","223056438","28803555","112934796")


'''
12. 该文本里，谁发的微博内容长度最长 （要求：输出用户的uid，字符串格式。）
'''
max_len = 0
max_uid = list()

for info in info_list:
    current_len =  len(info["content"])
    uid = info["uid"]
    if current_len > max_len:
        max_len = current_len
        del max_uid[:]
        max_uid.append(uid)
    elif current_len == max_len:
        max_uid.append(uid)

print max_uid[0] 

'''
13. 该文本里，谁转发的URL最多 （要求：输出用户的uid，字符串格式。）
'''

rt_uids_list = [ x["rt_uid"] for x in info_list if len(x["rt_uid"]) > 0 ]
rt_uids_set = set(rt_uids_list)
rt_uid_cnt_dict = { x:rt_uids_list.count(x) for x in rt_uids_set}
rt_uids_cnt_list = rt_uid_cnt_dict.items()
rt_uids_cnt_list.sort(reverse=True,key=lambda x:x[1])
print rt_uids_cnt_list[0][0]


'''
14. 该文本里，11点钟，谁发的微博次数最多。 （要求：输出用户的uid，字符串格式。）
'''

users_11clock = [ x["username"] for x in info_list if x["created_at"].split()[1].split(':')[0] == "11" ]

user_11clock_set = set(users_11clock)

users_cnt_dict = { x:users_11clock.count(x) for x in user_11clock_set }
users_cnt_list = users_cnt_dict.items()
users_cnt_list.sort(reverse=True,key=lambda x:x[1])
print users_cnt_list[0][0]


'''
15. 该文本里，哪个用户的源微博URL次数最多。 （要求：输出用户的uid，字符串格式。）
'''

uid_set = set([x["uid"] for x in info_list ])
uid_vurl_dict = { x:0 for x in uid_set }

for info in info_list:
    uid = info["uid"]
    uid_vurl_dict[uid] += 1

uid_vurl_list = uid_vurl_dict.items()

uid_vurl_list.sort(reverse=True,key=lambda x:x[1])
print uid_vurl_list[0][0]
