 
# 多线程 #


python里的多线程，不是真正意义上的多线程。

实际上是利用全局锁在任意的指定时间里切换线程，有且只有一个线程在运行。

## 1 建立多线程对象 ##

步骤 

	1.创建threading.Thread对象
	
	__init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None)
	
	2 start 开始执行进程
	
	
	3 join 阻塞等待进程

例子：
 

	import threading
	           
	def test(num):  
	    print num   
	           
	ts = []    
	           
	for i in xrange(0,15):
	    th = threading.Thread(target=test,args=[i])
	    th.start()  
	    ts.append(th)
	           
	           
	for i in ts:
	    i.join()
	           
	print "end" 


## 2 全局锁 GIL ##

由于python多线程中使用全局锁来管理，因此

**在任意一个指定的时间，有且只有一个线程在运行**
 

注意多线程不是线程安全的，操作共享资源还是要加锁的


## 3 多线程用在哪里 ##

 
在使用IO密集任务时使用多线程可以大大降低程序运行时间。



	import time
	import threading
	   
	def funa():
	    print "begin a"
	    time.sleep(2)
	    print "end a"
	   
	def funb():
	    print "begin b"
	    time.sleep(2)
	    print "end b"
	   
	beg = time.time()
	
	funa()
	funb()
	 
	print "use time : %f senconds." %  (time.time()-beg)
	 
	beg = time.time()
	 
	ta = threading.Thread(target=funa)
	tb = threading.Thread(target=funb)
	 
	ta.start()
	tb.start()
	                                                                                                       
	ta.join()
	tb.join()
	 
	print "use time : %f senconds." %  (time.time()-beg)

	
	结果： 	

	begin a
	end a
	begin b
	end b
	use time : 4.005526 senconds.
	begin a
	begin b
	end b
	end a
	use time : 2.006530 senconds.


 



## 4.io操作用到多线程？必须要lock，acquire release ##

	import threading
	mlock = threading.Lock() #锁对象
	num=0
	                                                                                                       
	def fun():
	    global num 
	    mlock.acquire() #加锁
	    num+=1
	    mlock.release() #解锁
	    print num 
	 
	for i in xrange(0,15):
	    th = threading.Thread(target=fun)
	    th.start()


## 5 rlock 可重入锁 ##

lock时，如果已经锁上了，就要等待锁释放


在Python中为了支持在**同一线程**中多次请求同一资源，python提供了“可重入锁”：threading.RLock。这个RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次require。直到一个线程所有的acquire都被release，其他的线程才能获得资源。 

	
	import threading
	mlock = threading.RLock() #r锁对象
	num=0                                                                                                  
	     
	def fun():
	    global num
	    mlock.acquire() #加锁
	    num+=1
	    mlock.acquire() #再加锁
	    print num
	    mlock.release()
	    mlock.release()
	     
	     
	for i in xrange(0,15):
	    th = threading.Thread(target=fun)
	    th.start()


##6 协程

1 使用yield的函数的返回值是迭代对，其中所有的值是yield的参数

2 yield的返回值由send来发送

3 next和send都会指向迭代对象中的下一个值 


	def func():
	    x = yield 1 #加入可迭代返回值中
	    print x
	    x = yield 2 #加入可迭代返回值中
	    print x
	    yield                                                       
	       
	m = func()
	print m.next()	
	print m.send("hello")
	print m.send("world")


	返回值:

	1
	hello
	2
	world
	None