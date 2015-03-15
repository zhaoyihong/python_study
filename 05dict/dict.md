# 字典： #

字典是**无序**的，它不能通过偏移来存取，只能通过键来存取。

字典 = {'key':value}

key：类似我们现实的钥匙，而value则是锁。一个钥匙开一个锁

## 特点： ##

内部没有顺序，通过键来读取内容，可嵌套，方便我们组织多种数据结构，并且可以原地修改里面的内容，

属于可变类型。

组成字典的键必须是不可变的数据类型，**比如，数字，字符串，元组等，列表等可变对象不能作为键.
**


## 1 创建字典。 { },dict()##

 

info = {'name':'lilei', 'age': 20}'

info = dict(name="lilei",age=20)   

	
	>>> info = {'name':'lilei', 'age': 20}
	>>> info
	{'age': 20, 'name': 'lilei'}

	>>> info = dict(name="lilei",age=20)    
	>>> print info
	{'age': 20, 'name': 'lilei'}
	 
 
## 2 添加内容   a['xx'] = 'xx'##


比如  info['phone'] = 'iphone5'

	>>> info = dict(name="lilei",age=20)
	>>> info["phone"] = "iphone5s" 
	>>> info
	{'phone': 'iphone5s', 'age': 20, 'name': 'lilei'}

## 3 修改内容 a['xx'] = 'xx'  ##

#### info['phone'] = 'htc' ####

	>>> info
	{'phone': 'iphone5s', 'age': 20, 'name': 'lilei'}
	>>> info["phone"] = "htc"
	>>> info
	{'phone': 'htc', 'age': 20, 'name': 'lilei'}
	 
#### update 参数是一个字典的类型，他会覆盖相同键的值 ####


info.update({'city':'beijing','phone':'nokia'})

htc 变成了nokia了

	>>> info
	{'phone': 'htc', 'age': 20, 'name': 'lilei'}
	>>> info.update({"phone":"nokia","city":"beijing"})
	>>> info
	{'phone': 'nokia', 'age': 20, 'name': 'lilei', 'city': 'beijing'}



## 4 删除 del,clear,pop ##

del info['phone'] 删除某个元素

info.clear()删除字典的全部元素

info.pop('name') 返回键名对应的值,并且从字典中将这个键删除掉


	>>> info
	{'phone': 'nokia', 'age': 20, 'name': 'lilei', 'city': 'beijing'}
	
	>>> del info["phone"]
	>>> info
	{'age': 20, 'name': 'lilei', 'city': 'beijing'}
	
	>>> info["phone"]
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	KeyError: 'phone'
	
	>>> info.clear()
	>>> info
	{}
	
	>>> info =  {'phone': 'nokia', 'age': 20, 'name': 'lilei', 'city': 'beijing'}
	>>> info.pop("phone")
	'nokia'
	>>> info
	{'age': 20, 'name': 'lilei', 'city': 'beijing'}
	>>> 


## 5 列表pop方法和字典pop方法的区别 ##


pop方法都是返回元素的值并且将该元素从对象中删除
当pop一个不存在的元素时都会报错

列表pop() 传入索引号
字典pop() 传入key

列表pop()可以不传入参数,默认返回最后一个元素
字典pop可以传入一个默认返回值,当key值不存在时,返回这个默认值

	
	>>> a = [1,2,3,4,5]
	>>> a.pop()
	5
	>>> a
	[1, 2, 3, 4]
	>>> a.pop(0)
	1
	>>> a
	[2, 3, 4]
	>>> a.pop(3)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	IndexError: pop index out of range



	>>> info =  {'phone': 'nokia', 'age': 20, 'name': 'lilei', 'city': 'beijing'} 
	>>> info.pop('phone')
	'nokia'
	>>> info
	{'age': 20, 'name': 'lilei', 'city': 'beijing'}
	>>> info.pop('xx') 
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	KeyError: 'xx'
	>>> info.pop('xx','yy')
	'yy'


 
## 6 in 和 has_key() 成员关系操作 ##

in 和 haskey()用来判断key是否在字典中

1 phone in info

2  info.has_key('phone')

	
	>>> info =  {'phone': 'nokia', 'age': 20, 'name': 'lilei', 'city': 'beijing'}
	>>> "phone" in info       
	True
	>>> info.has_key("iphone")
	False


## 7 keys,values,intems ##
 

keys(): 返回的是**列表**，里面包含了字典的所有键

values():返回的是**列表**，里面包含了字典的所有值

items：返回的是**列表**，里面包含了字典的所有键值对：[()]

	
	>>> info =  {'phone': 'nokia', 'age': 20, 'name': 'lilei', 'city': 'beijing'}
	>>> info.keys()
	['phone', 'age', 'name', 'city']
	>>> info.values()
	['nokia', 20, 'lilei', 'beijing']
	>>> info.items()
	[('phone', 'nokia'), ('age', 20), ('name', 'lilei'), ('city', 'beijing')]





## 8 get：从字典中获得一个值 ##

查询key的value有两种方法:

info['name']  返回value,如果key不存在则报错

info.get('name') 返回value,如果key不存在则报错

info.get('age2','22') 返回value,如果key不存在则返回默认值


get()方法的好处是可以设置默认值


	>>> info =  {'phone': 'nokia', 'age': 20, 'name': 'lilei', 'city': 'beijing'}
	>>> info['phone']
	'nokia'
	>>> info.get('phone')
	'nokia'
	>>> info.get('xx','yy')
	'yy'
