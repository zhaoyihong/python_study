#语句与数据结构应用


##1.最基本的迭代

使用for来迭代

	a = [1,2,3,4,5]
	for x in a:
	    print x

##2.如何迭代字典

字典是无序的，key是唯一的

	
	b = {"key1":"value1","key2":"value2"}                                           
	
	#方法1
	for i in b.keys():
	    print i,b[i]

	#方法2 
	for x,y in b.items():                                            
    print x,y    


## 3.如何为字典排序 ##

### 3.1 按照键来排序 ###
先将键取出来排序，再依据键来取值

	b = {"key2":"value2","key1":"value1"}
	key_list = b.keys()
	key_list.sort()
	for i in key_list:
	    print i,b[i]


### 3.2 按照值来排序 ###

先取出items，再依据值来排序
 
	b = {"key2":"value2","key1":"value1"}
	b_list = b.items();
	b_list.sort(key=lambda x:x[1])
	for x,y in b_list:
	    print x,y

## 4.字典根据键值查找键 ##

注意值不是唯一的，一个值可能对应N个键

	c = {"a":"m","b":"n","c":"m","d":"n"}
	m_keys = [] 
	for x,y in c.items():
	    if y == "m":
	        m_keys.append(x)
	            
	print m_keys 


## 5.sorted排序方法再议 ##

sort不改变原先的容器，返回排好序的list


	sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list


	s = list("python:helloworld!")
	a = sorted(s)
	print a
	b = sorted(s,reverse=True)
	print b

## 6.好玩的translate与maketrans ##


replace是一个个替换，使用翻译表就可以逐个替换

	>>> a = "12345132231"   
	>>> a.replace("123","abc")
	'abc45132231'
只能将123这个整体进行修改，如果要将1改为a，2改为b，c改为3，则需要replace多次

使用翻译表可以解决这个问题

	string模块中

创建翻译表

    maketrans(...)
        maketrans(frm, to) -> string
        
        Return a translation table (a string of 256 bytes long)
        suitable for use in string.translate.  The strings frm and to
        must be of the same length.


进行翻译

    translate(s, table, deletions='')
        translate(s,table [,deletions]) -> string
        
        Return a copy of the string s, where all characters occurring
        in the optional argument deletions are removed, and the
        remaining characters have been mapped through the given
        translation table, which must be a string of length 256.  The
        deletions argument is not allowed for Unicode strings.
    
翻译的例子
    
	>>> g = string.maketrans("123","abc")
	>>> a = "12345132231"                
	>>> b = a.translate(g)  #第一个参数是a.self,第二个参数是g 
	>>> print b
	abc45acbbca

translate还可以进行逐个删除

	>>> a = "12345132231"   
	>>> g = string.maketrans(" "," ") #空的替换
	>>> b = a.translate(g,'1')        
	>>> b
	'23453223'
	>>> b = a.translate(g,'123')
	>>> b
	'45'
	



## 7.一个新的语句，with ##

with带来方便

在with下建立的对象会在with结束时释放掉



	file = open("/tmp/foo.txt")
	try:
	    data = file.read()
	finally:
	    file.close()

with版：

	with open("/tmp/foo.txt") as file:
    	data = file.read()


with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。

紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量。当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。
	