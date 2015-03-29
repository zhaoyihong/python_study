 
#  异常 #

exception,中译异常，保守派的圣杯，被滥用的良药。


## 1.出错的东西们，他们出了什么错. ##


他们出错 = 被抛出了异常



## 2.我们不想让他们出错，该怎么办。 ##

exception来了。


## 3.基本语法
	
try，except，else，finally


	a = [1,2,3,4,5]                              
	    
	try:
		#可能会抛出异常的代码
	    print a[5]                               
	except:                                      
	    print "try语句块中出错了执行这里"
	    sys.exit(-1)
	else:
	    print "try语句块中没出错执行这里"
	finally:
	    print "无论如何都会执行这里，即使中途exit了"

	print "中途没有exit才会执行到这里"


如果没有try，一旦发生异常，就在异常的句子处直接退出程序

如果有try，一旦发生异常，就在异常的句子处跳到except中，try块中没有执行到的语句不会执行



## 4.我们为什么不让他出错？ ##

在开发阶段，我们是可以让任何东西出错的。



## 5.什么时候用，怎么用？ ##

我们什么时候用异常？ -- 不得不用的时候。


异常怎么用？

1.我们知道会有哪些问题，分析问题，得到这些问题会抛出的指定异常

2.捕获正确的异常，不要直接 try except
  	
3.异常的处理，要合理。要有日志。



	sth_url = "http://xxsdsdsd"
	              
	try:          
	    d = urllib.open(sth_url)
	except IOError:                                           
	    print "该url无法打开"
	except:       
	    print "其他错误"
	else:         
	    content = d.read()
	    print content
	    d.close()


## 6 异常的几点注意 ##

一个try就有一个except

### 1.1 不要没事就乱用异常 ###

		慎用异常： 1.找到python的内置异常
		         2。理解python的内置异常分别对应什么情况
			     3.阅读你的代码，找到你的代码里可能会抛出内置异常的地方
		         4.仅对这几行代码做异常处理

	假设你无法知道你的代码会抛出什么异常，那么，你的异常处理便是无效的。	-》 准确了解你的代码情况。



### 1.2 不要一个代码块，大try完事。 ###

### 1.3 好吧，想try all exception？sys.exc_info() ###

懒人用法

	try:
	    a=3
	    assert a==4
	except:
	    exc = sys.exc_info()
	    print exc

结果：

(<type 'exceptions.AssertionError'>, AssertionError(), <traceback object at 0x7fb61f855638>)


### 1.4 logging如何使用呢 ###


	'''
		配置日志
	'''
	import logging
	logger = logging.getLogger() #创建一个logging对象
	hdlr = logging.FileHandler('testlog.txt') #创建存放日志的文件句柄
	formater = logging.Formatter('%(asctime)s %(levelname)s %(message)s') #设置日志格式
	hdlr.setFormatter(formater) #文件绑定格式
	logger.addHandler(hdlr)     #logging对象绑定文件句柄
	#设置日志的最低等级 CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
	 logger.setLevel(logging.NOTSET) 
 
 
	try:
	    a=3
	    assert a==4
	except: 
	    exc = sys.exc_info()
	    logging.debug(exc) #将异常信息写入logger
                                             



## 7 断言，一种开发期时检定代码的方式 ##

只断言绝对不能出现的错误 twisted


 先断言绝对不能发生的错误，然后，再去处理错误 （异常）

 格式：

  	assert 表达式   ,   "出错以后抛出的message"

 
	assert a==4,"a!=4"


## 8 代码友好，自动处理垃圾,with. ##


自动关闭文件
                     
	with open("a.txt","r") as a:
	    print a.read()

自动释放对象 ： 

要求类中必须有__enter__和__exit__方法

进入时调用enter 出去时调用exit


	                     
	class sth(object):
	                     
	    def __enter__(self):
	       print "__enter__"
	                     
	    def __exit__(self,type,value,traceback):
	       print "__exit__"
	                     
	with sth() as s:  
	    print "in with"       
	
	结果

	__enter__
	in with
	__exit__


## 9 自己定义异常？继承exception类 ##
	
这里写个简单的。。。




	class MyException(Exception):
	              
	    def __init__(self,error,msg):
	       self.args = (error,msg)
 
	              
	try:          
	    raise MyException(100,"my exception")
	except Exception as e:
	    print str(e)
	 