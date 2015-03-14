 
# 列表 #


 
##  特点 ##
1. 有序的集合
2. 通过偏移来索引，从而读取数据
3. 支持嵌套
4. 可变的类型

 

## 1 切片: ##

 


+ 正向索引
+ 反向索引
+ 默认索引


    	a = [1,2,3，4，5，6，7］
		>>> print a[1:4:1]   
		[2, 3, 4]
 
    	>>> print a[4:1:-1]
    	[5, 4, 3]

    	>>> print a[0:4]
    	[1, 2, 3, 4]
 

## 2添加操作： ##
 

***Extend***  接受参数并将该参数的**每个元素**都添加到原有的列表中，原地修改列表而不是新建列表

	>>> a = [1,2,3]
	>>> b = [4,5,6]
	>>> print id(a)
	139808949914368
	>>> a.extend(b)
	>>> print a
	[1, 2, 3, 4, 5, 6]
	>>> print id(a)
	139808949914368

***Append*** :添加任意对象到列表的末端,被添加的对象作为list的一个元素

	>>> a=[1,2,3]
	>>> b=[4,5,6]
	>>> print id(a)
	20760984
	>>> a.append(b)
	>>> print a
	[1, 2, 3, [4, 5, 6]]
	>>> print id(a)
	20760984


***Insert***: 插入任意对象到列表中，可以控制插入位置,被插入的对象作为list的一个元素
	
	>>> a=[1,2,3]  
	>>> b=[4,5,6]  
	>>> a.insert(0,b)
	>>> print a
	[[4, 5, 6], 1, 2, 3]
 

## 3 修改： ##
修改列表本身只需要直接赋值操作就行。

	>>> A = [1,2,3]
	>>> A[0]="hahaha"
	>>> print A
	['hahaha', 2, 3]

 

## 4 删除操作： ##

***Del*** ：我们通过索引删除指定位置的元素。

	>>> a=[1,2,3]
	>>> del a[0]
	>>> print a
	[2, 3]


***Remove***：移除列表中指定值的第一个匹配值。如果没找到的话，会抛异常。
    
    >>> a = [ 1, 2, 3, 4, 4, 2]
    >>> a.remove(2)
    >>> print a
    [1, 3, 4, 4, 2]

***Pop***：返回最后一个元素，并从list中删除它。

    >>> a = [1,2,3]
    >>> a.pop()
    3
    >>> print a
    [1, 2]
     

## 5 成员关系： ##

in not in我们可以判断一个元素是否在列表里。 

返回一个bool类型，元素在列表里返回true，否则返回fasle.


	>>> a = [1,2,3]
	>>> 1 in a
	True
	>>> 4 in a
	False
 
## 6 列表推导式： ##


**[expr for iter_var in iterable]**

首先迭代iterable里所有内容，每一次迭代，都把iterable里相应内容放到iter_var中，再在表达式中应用该iter_var的内容，最后用表达式的计算值生成一个列表。

比如我们要生成一个包含1到10的列表



	>>> range(1,11)
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	>>> [ 2*x+1 for x in range(1,11) ]
	[3, 5, 7, 9, 11, 13, 15, 17, 19, 21]


**[expr for iter_var in iterable if cond_expr]**

加入了判断语句，只有满足条件的内容才把iterable里相应内容放到iter_var中，再在表达式中应用该iter_var的内容，最后用表达式的计算值生成一个列表。

要生成包含1到10的所有奇数列表。

	 >>> [ x for x in range(1,11)  if x%2 != 0] 
	[1, 3, 5, 7, 9]
	>>> range(1,11,2)
	[1, 3, 5, 7, 9]
	 

## 7 排序翻转：sort,reverse ##

***sort***: 使列表排序 , 这个方式直接修改原列表。他的返回值为none


	>>> a = [2, 3, 1, 9 ,0]
	>>> b = a.sort()
	>>> print a
	[0, 1, 2, 3, 9]
	>>> print b
	None
 

***reverse***：反转一个list, 他的返回值为none

	 >>> print a
	[0, 1, 2, 3, 9]
	>>> b=a.reverse()
	>>> print a
	[9, 3, 2, 1, 0]
	>>> print b
	None
 

## 8.内置list方法: ##


list函数 : 返回一个列表，参数是可迭代对象。里面输出的内容还是保持了传入的可迭代对象的元素和顺序。


如果参数为空，则返回一个空的列表


	>>> a = "abc"
	>>> list(a)
	['a', 'b', 'c']


## 9.xrange和range的具体区别: ##

### range 和 xrange的用法： ###

range(开始，结束，步长)
range 它生成一个list对象。

xrange(开始，结束，步长)
xrange 它生成一个xrange对象。

区间都是 [ 开始,结束 )


	>>> range(10)
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

	>>> a = range(1,10,2)
	>>> print a
	[1, 3, 5, 7, 9]
	>>> print type(a)
	<type 'list'>
	>>> b = xrange(1,10,2)
	>>> print a
	[1, 3, 5, 7, 9]
	>>> print type(b)
	<type 'xrange'>


### 比较: ###

range: 直接生成一个列表对象。

xrange: 它是生成一个xrange对象.



### xrange的用法： ###

+ 当我们需要操作一个非常大的数据，而且内存比较吃紧的时候，我们可以用xrange来操作省内存。
+ xrange一般用在循环里面，比如我们只需要操作部分数据的话，而不是返回全部元素来完成操作，推荐用xrange,效率更高。

比如下面的程序中,使用range需要生成1000个数据,而使用xrange只需要生成10个数据

	
	for m in range(1000)：
	
	    if m == 10:
	
	      print 'sss'
	
	      break

	
	for m in xrange(1000):
	
	    if m == 10:
	
	      print 'sss'
	
	      break


xrange只能索引不能切片

	>>> b = xrange(1,10)
	>>> print b[0]
	1
	>>> print [:2]
	  File "<stdin>", line 1
	    print [:2]
	           ^
	SyntaxError: invalid syntax


## 10.列表推导式之再应用。 ##

 

例1: 取出1-10的所有值的平方。

	>>> [x*x for x in range(1,11)]
	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	 


例2  里面生成东西不只是数字。

生成字符串 

	>>> ['the %s' % d  for d in xrange(10)]
	['the 0', 'the 1', 'the 2', 'the 3', 'the 4', 'the 5', 'the 6', 'the 7', 'the 8', 'the 9']

生成元组  

	>>> [(x,y) for x in range(0,2) for y in range(0,2)] 
	[(0, 0), (0, 1), (1, 0), (1, 1)]

生成字典  举例
	
	>>> dict([(x,y) for x in range(3) for y in range(2)])
	{0: 1, 1: 1, 2: 1}

## 11 翻来覆去之再谈引用 ##

 
		
		>>> a = ['i','am','lilei']
		>>> b = a
		>>> a[2] = 'laowang'
		>>> print a
		['i', 'am', 'laowang']
		>>> print b
		['i', 'am', 'laowang']
		>>> print id(a)
		139808950104864
		>>> print id(b)
		139808950104864
		>>> del b
		>>> print a
		['i', 'am', 'laowang']

		>>> c = a
		>>> print c
		['i', 'am', 'laowang']
		>>> del c[:]
		>>> c
		[]
		>>> a
		[]

 

1 del a 删除列表对象的引用

2 del a[:] 清空列表对象里的元素


要改变指向的对象,要使用索引或者切片
