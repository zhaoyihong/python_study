# 元组： tuple #

## 特点： ##

1 有序的集合

2 通过偏移来取数据

3 属于不可变的对象，不能在原地修改内容，没有排序，修改等操作。

## tuple类型转换 ##

	>>> a = [1,2,3]
	>>> a[0] = 5
	>>> b = tuple(a)
	>>> type(b)
	<type 'tuple'>
	>>> a
	[5, 2, 3]
	>>> b
	(5, 2, 3)

## 那为什么有列表还要有元组呢 ##

 元组不可变的好处。保证数据的安全，比如我们传给一个不熟悉的方法或者数据接口，
 确保方法或者接口不会改变我们的数据从而导致程序问题。
 


 
 