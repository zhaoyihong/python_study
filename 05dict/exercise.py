#!/usr/bin/env python
# coding=utf-8

'''
##习题7：
用字典的方式完成下面一个小型的学生管理系统。

1 学生有下面几个属性：姓名，年龄，考试分数包括：语文，数学，英语得分。
比如定义2个同学：
姓名：李明，年龄25，考试分数：语文80，数学75，英语85
姓名：张强，年龄23，考试分数：语文75，数学82，英语78
2 给学生添加一门python课程成绩，李明60分，张强：80分
3 把张强的数学成绩由82分改成89分
4 删除李明的年龄数据
5 对张强同学的课程分数按照从低到高排序输出。
6 外部删除学生所在的城市属性，不存在返回字符串 beijing
'''
#1
stu_info = {"liming":{"name":"李明","age":25,"score":{"chinese":80,"math":75,"english":85}}}
stu_info["zhangqiang"] = { "name":"张强","age":23,"score":{"chinese":75,"math":82,"english":78}}
print stu_info
#2 
stu_info["liming"]["score"]["python"] = 60
stu_info['zhangqiang']['score']['python'] = 80
print stu_info
#3
stu_info['zhangqiang']['score']['math']=89
print stu_info
#4
del stu_info['liming']['age']
print stu_info
#5
zq_score=stu_info['zhangqiang']['score']
scores = zq_score.values()
scores.sort()
print scores
#6
print stu_info.get('liming').pop('city','beijing')
print stu_info.get('zhangqiang').pop('city','beijing')





