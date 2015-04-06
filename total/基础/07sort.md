
 sort用法

### sort函数原型 ###

	sort(...)
	 L.sort(cmp=None, key=None, reverse=False)  -- stable sort *IN PLACE*;
	 
	cmp(x, y) -> -1, 0, 1

### 简单的sort: ###

无参数 sort()


以默认方式进行排序,整数以数字大小,字符串以字典序

	>>> a
	[1, 2, 3, 4]
	>>> a.sort(None,None,True)
	>>> print a
	[4, 3, 2, 1]
	>>> b = ['1020','99','33','2014']
	>>> b.sort()
	>>> b
	['1020', '2014', '33', '99']

默认的排序方式是cmp函数

	>>> cmp(1,2)
	-1
	>>> cmp(2,2)
	0
	>>> cmp('a','b')
	-1
	>>> help(cmp)
	Help on built-in function cmp in module __builtin__:
	
	cmp(...)
    cmp(x, y) -> integer
    
    Return negative if x<y, zero if x==y, positive if x>y.

### lambda表达式 ###

 因为cmp和key都是函数,cmp是两参数的函数,key是单参数的函数,使用lambda表达式可以简洁写出语句

lambda表达式格式是 lambda [arg1[,arg2,arg3....argN]]:expression

无参的:
	
	>>> (lambda:True)()                
	True

单参数

	>>> (lambda x:x%2)(10)
	0

二参数

	>>> (lambda x:x%2)(1) 
	1
	>>> (lambda x,y:x-y)(1,2)
	-1
	>>> 

### 设置比较方法 cmp ###


将cmp设置为一个两个参数的函数


下面的例子中cmp(y,x) 表示以默认相反的方式比较

这里要注意的是cmp的效率比较低,直接设置reverse比这个要快

	>>> a=[1,2,3,4,5]
	>>> a.sort(cmp=lambda x,y:cmp(y,x))
	>>> a
	[5, 4, 3, 2, 1]


将偶数排在前面

	>>> a.sort(cmp=lambda x,y:x%2-y%2) 
	>>> a
	[4, 2, 5, 3, 1]

如果需要更复杂的逻辑可以直接定义函数:

	 a = [ 2 ,3 ,1, 4, 5, 7,0]
	        
	#偶数排在奇数前面,如果奇偶性相同以数字大小排序        
	def my_cmp(x,y):                                                                                       
	    n = x%2 - y%2      
	    if n != 0:         
			return n       
	    else:              
		  return x-y     
	                       
	a.sort(cmp=my_cmp)     
	print a    

当然上面例子不够复杂,可以用下面lambda来表示

	a.sort(cmp=lambda x,y:x-y if x%2==y%2 else x%2-y%2)

 

### 设置比较值 ###

 
将比较值转化为整数


	>>> b=["2013","1999","1024"]
	>>> b.sort()
	>>> b.sort(key=int)
	>>> b
	['1024', '1999', '2013']


	>>> b=["2013","1999","1024"]
	>>> b.sort(key=lambda x:int(x))
	>>> b
	['1024', '1999', '2013']


### 多级排序 ###

将比较值(key)设置为多个就可以了

key=operator.itemgetter(1,2) 返回一个能够返回指定元素的元组



	 |  itemgetter(item, ...) --> itemgetter object
	 |  
	 |  Return a callable object that fetches the given item(s) from its operand.


这个函数可以这么理解

	>>> fun=operator.itemgetter(1,2)
	>>> fun((1,2,3,4,))
	(2, 3)
	>>> fun([1,2,3,4])
	(2, 3)
	>>> fun("helloworld")
	('e', 'l')
	>>> 


在sort中使用key=operator.itemgetter(1,2) ,表示比较值是list中每个元素中的(第一个元素,第二个元素)组成元组


	>>> import operator
	>>> a = [(2,3,5),(1,2,4),(2,5,3)]
	>>> a.sort(key=operator.itemgetter(1,2))
	>>> a
	[(1, 2, 4), (2, 3, 5), (2, 5, 3)]



### 设置reverse ###

reverse=True时反转排序

	>>> a=[1,2,4,3,5]
	>>> a.sort(reverse=True)
	>>> a
	[5, 4, 3, 2, 1]


### 将字典以value值排序打印出键值对来 ###

首先将字典items()函数的方式取出键值对的list
然后再设置sort中key参数

 
lambda写法

	>>> c={'a':2,'b':1,'c':3,'d':4}
	>>> d=c.items()
	>>> d
	[('a', 2), ('c', 3), ('b', 1), ('d', 4)]
	>>> d.sort(key=lambda x:x[1])
	>>> d
	[('b', 1), ('a', 2), ('c', 3), ('d', 4)]
	>>> d.sort(key=lambda x:x[1],reverse=True)
	>>> d
	[('d', 4), ('c', 3), ('a', 2), ('b', 1)]


operator.itemgetter 写法

	>>> c={'a':2,'b':1,'c':3,'d':4}
	>>> d=c.items() 
	>>> d
	[('a', 2), ('c', 3), ('b', 1), ('d', 4)]
	>>> d.sort(key=operator.itemgetter(1))
	>>> d
	[('b', 1), ('a', 2), ('c', 3), ('d', 4)]

	
		 

##sorted函数

sorted函数返回一个已排序的list,但是不改变原先的可迭代对象

函数原型

	sorted(...)
	    sorted(iterable, cmp=None, key=None, reverse=False) --> 
		new sorted list

操作的对象的必须是一个可迭代对象(string,list,tuple)
	
	
	>>> a = [2,3,4,1,5]
	>>> sorted(a)
	[1, 2, 3, 4, 5]
	>>> a
	[2, 3, 4, 1, 5]
	>>> c = tuple(a)
	>>> sorted(c)
	[1, 2, 3, 4, 5]
	>>> d = "12345"
	>>> sorted(d)
	['1', '2', '3', '4', '5']


其他三个参数的用法和原先的一样



##字典排序

python 字典（dict）的特点就是无序的，按照键（key）来提取相应值（value），如果我们需要字典按值排序的话，那可以用下面的方法来进行：


### 1 下面的是按照value的值从大到小的顺序来排序。 ###

	dic = {'a':31, 'bc':5, 'c':3, 'asd':4, 'aa':74, 'd':0}
	dict= sorted(dic.iteritems(), key=lambda d:d[1], reverse = True)
	print dict

输出的结果：
[('aa', 74), ('a', 31), ('bc', 5), ('asd', 4), ('c', 3), ('d', 0)]



### 2 对字典按键（key）排序： ###

	dic = {'a':31, 'bc':5, 'c':3, 'asd':4, 'aa':74, 'd':0}
	dict= sorted(dic.iteritems(), key=lambda d:d[0]) d[0]表示字典的键
	print dict

