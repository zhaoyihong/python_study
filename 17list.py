#!/usr/bin/python
#coding=utf-8
#author:zhaoyihong
#email:zhaoyihong@126.com
#date:2014-04-10

'''
列表

有序数列合集
用 [ ]括起来,用逗号间隔每个数据项
数据项可以是不同类型
list里可以有list为其数据项


'''

li1 = [1,2,3,4]
print type(li1)

li2 = [1,'abc','c',1.2345,[1,2,3]]
#列表元素
print li2[4]
#列表长度
print len(li2)

'''
列表可被修改
可动态填充长度不固定

'''


#修改 赋值
li2[0] = 100
print li2[0]

li2[1] = li2[1].replace('c','v')
print li2[1]
print li2  #[100, 'abv', 'c', 1.2345, [1, 2, 3]]


#切片 [start:end:step]
li3 = li2[:3]
print li3 #[100, 'abv', 'c']
li4 = li2[:-3:-1]
print li4 #[[1, 2, 3], 1.2345]


#for in list
for ch in li2:
	print ch


#添加元素
'''
记住 不可以对超出范围的元素赋值

添加元素 
	append(Object) 
	insert(index,object) befor index

'''
li2.append(123)
print li2


li2.insert(0,'begin')
li2.insert(len(li2),'end')
print li2 #['begin', 100, 'abv', 'c', 1.2345, [1, 2, 3], 123, 'end']



'''
转化为列表
list()
并在b前插入m

索引 index()
'''
li3 = list('www.baidu.com')
print li3
li3.insert(li3.index('b'),'m')
print li3# ['w', 'w', 'w', '.', 'm', 'b', 'a', 'i', 'd', 'u', '.', 'c', 'o', 'm']


'''
range(start,end,step)
产生列表
'''
li4 = range(1,10)
print li4 #[1, 2, 3, 4, 5, 6, 7, 8, 9]


'''
extend 扩展列表
将另一个列表和本列表合并
	注意 : 如果用append,则被合并的列表只是作为一个元素
 L.extend(iterable) 
'''
li4.extend(li3)
print li4  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 'w', 'w', 'w', '.', 'm', 'b', 'a', 'i', 'd', 'u', '.', 'c', 'o', 'm']



'''
count()
统计数据项个数
'''
print li4.count('w') #3




'''
删除元素
remove(object)

'''
li4.remove('w')
print li4 #[1, 2, 3, 4, 5, 6, 7, 8, 9, 'w', 'w', '.', 'm', 'b', 'a', 'i', 'd', 'u', '.', 'c', 'o', 'm']



'''
删除元素
del(index)
'''
del li4[0]
print li4 #[2, 3, 4, 5, 6, 7, 8, 9, 'w', 'w', '.', 'm', 'b', 'a', 'i', 'd', 'u', '.', 'c', 'o', 'm']


'''
删除元素
pop()
删除最后一个

'''
li5 = li4.pop()
print li4 #[2, 3, 4, 5, 6, 7, 8, 9, 'w', 'w', '.', 'm', 'b', 'a', 'i', 'd', 'u', '.', 'c', 'o']
print li5 #m

'''
reverse()
逆序
'''
li4.reverse()
print li4 #['o', 'c', '.', 'u', 'd', 'i', 'a', 'b', 'm', '.', 'w', 'w', 9, 8, 7, 6, 5, 4, 3, 2]
#有趣的逆序还可以这样
print li4[::-1]#[2, 3, 4, 5, 6, 7, 8, 9, 'w', 'w', '.', 'm', 'b', 'a', 'i', 'd', 'u', '.', 'c', 'o']



