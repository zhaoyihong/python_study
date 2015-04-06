

# 集合： set#

集合是**没有顺序**的概念。所以不能用切片和索引操作。 

集合中没有重复元素

## 1 创建集合。 ##

	>>> a = {"a","b","c"}
	>>> type(a)
	<type 'set'>
 

set():可变的


frozenset()：不可变的,不能进行添加删除操作

	
	
	>>> a = set('helloworld')
	>>> print a
	set(['e', 'd', 'h', 'l', 'o', 'r', 'w'])
 
	 
	>>> b = frozenset('helloworld') 
	>>> print b
	frozenset(['e', 'd', 'h', 'l', 'o', 'r', 'w'])
 
## 2 添加操作： add，update ##

add 将对象作为一个整体添加到集合中 (像是list里面的insert和append)


	>>> a = set("abc")
	>>> a
	set(['a', 'c', 'b'])
	>>> a.add("python")
	>>> a
	set(['a', 'python', 'c', 'b'])


update 将对象的每个元素都添加到集合中  (像是list里面的extend)

	>>> b = set("abc")
	>>> b.update("python")
	>>> b
	set(['a', 'c', 'b', 'h', 'o', 'n', 'p', 't', 'y'])

## 3 删除 remove ##
	
remove方法可以删除集合中已有的元素

如果删除集合中没有的元素会报错,所以需要使用in,not in方法检查是否在集合中

	>>> b = set("abcdefg")
	>>> b
	set(['a', 'c', 'b', 'e', 'd', 'g', 'f'])
	>>> b.remove("b")
	>>> b
	set(['a', 'c', 'e', 'd', 'g', 'f'])
	>>> b.remove("on")
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	KeyError: 'on'

## 4 成员关系 in,not in ##
	
	>>> a = set("abcdefg")
	>>> a
	set(['a', 'c', 'b', 'e', 'd', 'g', 'f'])
	>>> "x" in a
	False
	>>> "a" in a 
	True
	>>> "a" not in a
	False


## 6 交集，并集，差集 & | - ##

 
a&b : a,b的交集 ,a,b中都出现的元素
 
a|b : a,b的并集 , a,b中所有的元素

a - b : a,b的差集 : a 中的元素 除去b中的元素
 

	
	>>> a = set("abcd") 
	>>> b = set("cdef")
	>>> a & b
	set(['c', 'd'])
	>>> a |  b
	set(['a', 'c', 'b', 'e', 'd', 'f'])
	>>> a -  b
	set(['a', 'b'])
	>>> b - a
	set(['e', 'f'])


## 7 set去重 :##

可以利用set去除list中的重复元素

	>>> a = list("helloworld")
	>>> a
	['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
	>>> a = list(set(a))
	>>> a
	['e', 'd', 'h', 'l', 'o', 'r', 'w']


 

## 8 是否相等

判断2个集合是否相等，之和元素本身有关，和顺序无关。

	>>> a = {"a","b","c"}
	>>> b = {"b","a","c"}
	>>> a == b
	True


##9 与字符串间的相互转化

	>>> a=set("helloworld")
	>>> a
	set(['e', 'd', 'h', 'l', 'o', 'r', 'w'])

	>>> "".join(a)
	'edhlorw'
