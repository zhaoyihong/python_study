# 模块 #



## 1 模块的引入 ##

在Python中用关键字import来引入某个模块，比如要引用模块math，就可以在文件最开始的地方用import math来引入。在调用math模块中的函数时，必须这样引用：


	模块名.函数名


调用函数必须加上模块名。

 
	import math
	
	#这样会报错
	print sqrt(2)
	
	#这样才能正确输出结果
	print math.sqrt(2)
 

只引入模块中的某个函数


	from 模块名 import 函数名1,函数名2....



来实现，当然可以通过不仅仅可以引入函数，还可以引入一些常量。通过这种方式引入的时候，调用函数时只能给出函数名，不能给出模块名，但是当两个模块中含有相同名称函数的时候，后面一次引入会覆盖前一次引入。 


如果想一次性引入math中所有的东西，还可以通过from math import *来实现，但是不建议这么做。


## 2 定义自己的模块 ##


在Python中，每个Python文件都可以作为一个模块，模块的名字就是文件的名字。

比如有这样一个文件test.py，在test.py中定义了函数add：
	
	#test.py
	
	def add(a,b):
	    return a+b


那么在其他文件中就可以先import test，然后通过test.add(a,b)来调用了，当然也可以通过from test import add来引入。


	import test                  
	                             
	                             
	if __name__ == "__main__":                                                     
	    print test.add(100,100)
	                             


## 3 从哪里找模块 ##


pypi模块库 [https://pypi.python.org/pypi](https://pypi.python.org/pypi)


## 4 我们应该首先选择标准库 ##

python标准库 [https://docs.python.org/2.7/](https://docs.python.org/2.7/)


## 5 常用模块 ##


网络模块	urllib urllib2
	
时间模块	datetime time

处理系统命令	os

对象序列化	pickle 

数据库	bsddb

日志	logging




