#!/usr/bin/env python
# coding=utf-8


'''

列表a = [11,22,24,29,30,32]

1 把28插入到列表的末端

2 在元素29后面插入元素57

3 把元素11修改成6

3 删除元素32

4 对列表从小到大排序

'''

a = [11,22,24,29,30,32]
#1
a.append(28)
print a
#2 
a.insert(a.index(29)+1,57)
print a
#3
a[a.index(11)] = 6
print a
#4
a.remove(32)
print a
#5 
a.sort()
print a


'''
列表b = [1,2,3,4,5]

1 用2种方法输出下面的结果：

[1,2,3,4,5,6,7,8]

2 用列表的2种方法返回结果：[5,4]

3 判断2是否在列表里

'''

#1
b = [1,2,3,4,5]
c =  b + [6,7,8]
print c

b.extend([6,7,8])
print b
#2
b = [1,2,3,4,5]
print b[-1:-3:-1]

d = []
d.append(b.pop())
d.append(b.pop())
print d

#3
print 2 in b 


'''

##习题3：

b = [23,45,22,44,25,66,78]

用列表解析完成下面习题：

1 生成所有奇数组成的列表

2 输出结果: ['the content 23','the content 45']

3 输出结果: [25, 47, 24, 46, 27, 68, 80]

'''
b = [23,45,22,44,25,66,78] 

#1
print [x for x in b if x%2 != 0]
#2
print ['the content %s' % x for x in b[:3]]
#3
print [x+2 for x in b]


'''
##习题4：


用range方法和列表推导的方法生成列表：


[11,22,33]

'''
print range(11,34,11)
print [ x*11 for x in range(1,4) ]



