# python语句讲解  #

## 1.print语句 ##

### 1.1 基本输出 ###
	>>> print "hello" 
	hello

单独的print就是输出一个空行

### 1.2 print的逗号 ###

逗号表示一个空格
	>>> print "a","b"
	a b

print以逗号结尾时,不换行,结尾时空格
	print "hello",
	print "world" 
结果是
	hello world

### 1.3 输出到文件 >>为重定向 ###
	>>> file = open("abc.txt","w")
	>>> print >> file,"helloworld\n"
	>>> file.close()


## 2.控制流语句（control flow） ##
 
  由条件和执行代码块组成。  

 （冒号与4个空格永不忘） 


 
建议使用如下格式:


	x=a+b
	if x:
	    print "a+b==3"
	else:
	    print "a+b!=3"


不建议是否如下格式:

	 
	if a+b == 3:
	    print "a+b==3"
	else:
	    print "a+b!=3"




## 3.布尔值 ##
 
True  False


### 布尔值的几个最基本运算符 ###
 
  and 与操作

  or  或操作

  is 检查共享

  is检查两个对象**是否引用同一个对象**

	>>> True is True
	True
	>>> 5 is True     
	False
	>>> "2333" is True 
	False
	>>> a=100
	>>> b=100
	>>> a is b
	True
	
	
 == 检查值


 not 逻辑反转

	>>> not False
	True
	>>> not True
	False
	>>> not not False
	False


 其他若干比较符号


## 4.if语句 （控制流语句） ##

	
### 4.1 if的组成 if else elif pass ##

if 与 elif 替代了switch  (python中没有switch)

	
	if x == 10:
	    print "you guess it!"
	elif x > 10:
	    print "x is too large "
	else:
	    print "x is too small"


pass 表示什么都不执行 


### 4.2 奇技淫巧 三元表达式 ##


#### 4.2.1 x if  else ####
 
	a=-10                  
	x = a if a>0 else -a   
	print x                
	                       
	a=100                  
	b=200                  
	c = a-b if a>b else b-a                                               
	print c  

结果是

	10
	100


#### 4.2.2 活用list   ####

False表示0
True表示1

 
	>>> [3,4][False]
	3
	>>> [3,4][True] 
	4 


#### 4.2.3 三元表达式玩玩就好 ####





## 5 while #

 
### while的基本格式 ###

		while expression:
			statement(s)

### while的基本组成部分 ###


break 结束while


continue 跳出当前这次循环，但不结束while


else 结束while以后执行  (**中途break不会执行else**)


注意：普通应用里，while一定要给一个结束条件，否则就是传说中的死循环



	x=0
	while x<20:
	    x +=2
	    if x>10:
	        break;
	    print x,
	 
	print

结果

	2 4 6 8 10


## 6.for语句 ##


### for的基本格式 ###

	 for item in iterable：
		 statement（s）


###for的基本组成部分 ###

	这三个的功能和while中是一样的:

	break
	continue
	else 
	

注意：**for的最后一个迭代值将保留**


	a = [1,2,3,4,5]
	for x in a:
	    print x
	    if x==3:
			break
	                                                                                                       
	print x

结果:

	1
	2
	3
	3

常用用法

	for x in "i am lilei ha ha ha".split():
	    print x,
	print 

结果:

	i am lilei ha ha ha

## 4.布尔值再议 ##

### 4.1 惰性求值，需要时再求值。 ###


多个and的语句中:

True and False and True and False and True

上面语句执行到第二个False就返回False


使用时,我们可以将有大概率为False的条件放在前面



### 4.2 从左到右，从先到后。 ###


### 4.3 利用小技巧。or之默认值 ###


or可以设置默认值



