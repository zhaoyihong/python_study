#  函数 #

## 1.函数是抽象的第一步 ##

## 2.如何定义函数  ##

### 	2.1 def是关键词，括号冒号永不忘，无缩进无真相。 ###
### 	2.2 没有return的函数，不是大丈夫——不是真函数。 ###
### 	2.3 不写doc的函数，就像没有性别的人类。 ###


## 3.函数的参数魔法和陷阱 ##

### 3.1 如何定义参数 ###

	def sum(a,b=1):
    return a+b 
                
	print sum(100,200)
	print sum(100)  


### 3.2 参数的值是局部变量 ###

#### 3.2.1 参数只在函数内部有用 ####

	b = 3 #全局变量
	def func():
	    b = 4 #局部变量
	    print b
	 
	func()
	print b #3

#### 3.2.1 全局变量介绍，使用方法 ####

如果在函数中想使用全局变量，要先进行声明

声明方法： global 变量名

错误的写法 : global a = 100 (语法错误，声明不可以和其他操作混用)


	b = 3 #全局变量
	def func():
	    global b  #局部变量
	    b=4
	    print b                                                              
	     
	func()
	print b #4

###3.3 参数匹配

1.位置匹配 func(name)

2.关键字匹配 func(key=value)

3.收集匹配
	
	1.元组收集 *kargs  
	2.字典收集 **kwargs   

4.参数顺序


### 3.4 参数修改 ###

参数修改是可以影响到原值的，类似于c++的引用
 
不过这样修改实在是恶心


	def func2(l):
	    l.append(4)
	l = [1,2,3]                                                            
	func2(l)
	print l #[1,2,3,4]

### 3.5 **和 *，星星是字典，星是元组。 ###

**修饰的参数，会被当做是字典
*修改的参数，会被当做是元组
 

字典 -- 调用时使用名字匹配

	def func3(**kr):                                     
	    return kr
	print func3(c=1,b=2,a=3) #{'a': 3, 'c': 1, 'b': 2}

元组 -- 调用时使用位置匹配
	            
	def func4(*z):
	    return z
	print func4(1,2,[1,2,3],4,5) #(1, 2, [1, 2, 3], 4, 5)
          
字典和元组
             
	a,b = func5(1,2,3,a=1,b=2,c=3)
	print a,b   #(1, 2, 3) {'a': 1, 'c': 3, 'b': 2}

这个的实际应用是函数的**可变参数**
	
	def func7(a,b,*kargs):
	    print "a:%d,b:%d" % (a,b)
	    for i in kargs:
	        print i,
	    print
 
	func7(1,2,3,4,5,6,7) 

	结果
	a:1,b:2
	3 4 5 6 7


### 3.5 参数的类型检查


	def sum(a,b=1):
	    if isinstance(a,int) and isinstance(b,int):
	       return a+b 
	    else:
	   	   return "有些参数不是数字"
	

	isinstance(...)
	    isinstance(object, class-or-type-or-tuple) -> bool
	    
	    Return whether an object is an instance of a class or of a subclass thereof.
	    With a type as second argument, return whether that is the object's type.
	    The form using a tuple, isinstance(x, (A, B, ...)), is a shortcut for
	    isinstance(x, A) or isinstance(x, B) or ... (etc.).


## 4 函数的返回值 

默认返回值是None
 
可以返回1个或者多个值，也可以返回lambda表达式


##5 lambda表达式

1 lambda 是一个表达式

2 它没有名称，存储的也不是代码块，而是表达式

3 它可以被用作执行很小的功能，不能在里面使用条件语句



lambda表达式中可以使用**三元表达式和列表推导**


	d = lambda x:x-1 if x>0 else "error"
	         
	print d(1) #0
	print d(2) #1
	print d(0) #error


	d = lambda x:[(x,i) for i in range(1,5)]                                  
	print d(1) #[(1, 1), (1, 2), (1, 3), (1, 4)]
 

lambda表达式常和filter一起用

	filter(...)
	    filter(function or None, sequence) -> list, tuple, or string
	    
	    Return those items of sequence for which function(item) is true.  If
	    function is None, return the items that are true.  If sequence is a tuple
	    or string, return the same type, else return a list.

 	>>> a = range(1,11)
	>>> b = filter(lambda x:x>4,a)
	>>> print b
	[5, 6, 7, 8, 9, 10]


##6 递归函数

	def fab(i):
	    assert i>=0 
	    if i == 0 : 
	       return 0
	    elif i == 1:
	       return 1
	    else:  
	       return fab(i-1)+fab(i-2)
	              
	print fab(1)
	print fab(2)
	print fab(3)
	print fab(4)
	print fab(5) 