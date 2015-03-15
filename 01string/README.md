# 1 python一切皆为对象  #

     test = 4 表示 test是对4这个对象的引用
     test = 3 表示test 指向了3这个对象

# 2.数据类型的组成 #
	组成3部分。
	身份 id方法来看一看他的唯一标示符，内存地址靠这个哦！
	类型 type来看一看。
	值 数据项。
	python里一切都是指针

# 3常用基本数据类型. #
	int 整型
	boolean 布尔
	string  字符串
	list 列表
	tuple 元祖
	dict 字典


# 4.数据类型的可变和不可变 #
	不可变类型：int，string,tuple
	可变类型: list,dict
 
# 5.len之需注意 #
     英文是一个字节
     汉字是三个字节
     
     严格意义上说，str其实是字节串，它是unicode经过编码后的字节组成的序列。
	 
	 对UTF-8编码的str'汉'使用len()函数时，结果是3，
	 因为实际上，UTF-8编码的'汉' == '\xE6\xB1\x89'。

     
    >>> a="哈" 
    >>> print len(a)
    3
    >>> a=a.decode("utf-8")
    >>> print len(a)  
    1
    

# 13 字符编码 #
	str.deocde("utf-8") 将str转换为unicode编码 
	str.encode("utf-8") 将unicode编码还原为str
	str为字节串, unicode是字符串
	
	区别在于汉字字符(或者其他非英文数字)的字节数不同
	字符串中用汉字时,为了防止出错,请用utf-8解码
	
	>>> a="哈哈".decode("utf-8")
	>>> print a[0].encode("utf-8") 
	哈
	>>> a="哈哈"
	>>> print a[0]
	>>  #打印出来一个不可显示的字符
	
	处理完之后再encode回str类型





# 6.字符串前面跟着的小尾巴  #

    unicode字符串
    >>> b=u"哈"   
    >>> print len(b)
    1
    
    不转义
    >>> print r"\n"
    \n
    

# 7.访问子字符串  #

	成员有是有序排列的,可以通过下标偏移量访问到它的一个或者向个成员
	偏移量从0开始
	 

# 8.替换字符串 #
	   S.replace(old, new[, count]) -> string
	     注意字符串是不可修改的,只是新建了个对象
	
	>>> a="aabbccddeeff"       
	>>> b = a.replace("a","xx")  //替换全部
	>>> print b               
	xxxxbbccddeeff
	>>> c = b.replace("x","y",2)  //替换2个
	>>> print c
	yyxxbbccddeeff

# 9.字符串拼接 #

字符串拼接也是新建了个对象

## 1.超级丑陋之千万别用。 ##
	>>> print "aaa"+"bbb"
	aaabbb

## 2.可选方案之字符串模板  ##
    >>> print "my name is %s!"  % "lilei"
    my name is lilei!
    >>> print "my age is %d!"  % 20
    my age is 20!
    可以自动转换参数的类型
    >>> print "my age is %s!"  % 20 
    my age is 20!

    多个占位符后面跟一个元组
    >>> print "my name is %s,and my age is %d!" % ("lilei",20)
    my name is lilei,and my age is 20!
    
## 3 format方法 ##
	占位符是 {}
	>>> "my name is {},and my age is {}!".format("lilei",20)   
	'my name is lilei,and my age is 20!'
	
	占位符中可以加数字 {n} ,表示是第几个参数
	>>> "my name is {1},and my age is {0}!".format(20,"lilei")
	'my name is lilei,and my age is 20!'
	
	占位符可以加名字 {xxx}, 和后面的参数对应
	>>> "my name is {name},and my age is {age}!".format(age=20,name="lilei")
	'my name is lilei,and my age is 20!'


## 4.优秀的拼接方案 ##
	分隔符.join(list)
	
	>>> "".join([a,b,c])
	'aaaabbbbcccc'
	>>> "-".join([a,b,c])
	'aaaa-bbbb-cccc'


# 10.读写文本 #

## read / readline  ##
	
	>>> file=open("a.txt","w")
	>>> file.write("hi.\nsecond hi.")
	>>> file.close()
	>>> file=open("a.txt","r")      
	>>> file.readline()
	'hi.\n'
	>>> file.readline()
	'second hi.
	>>> file.seek(0)     //回到开头
	>>> file.read(100)  //读取100个字符
	'hi.\nsecond hi.'

## linecache库 ##
	import linecache
	
	>>> file=open("a.txt","w")
	>>> file.write("100\n200\n300\n400\n500\n")
	>>> file.close()
	>>> linecache.getline("a.txt",1)          
	'100\n'
	>>> print linecache.getline("a.txt",1)
	100
	
	>>> print linecache.getline("a.txt",2)
	200
	
	>>> print linecache.getline("a.txt",3)
	300
	
	>>> lines=linecache.getlines("a.txt")
	>>> print lines
	['100\n', '200\n', '300\n', '400\n', '500\n']




# 11 引号的区别 #

	' ' 和 " " 是没有区别的
	"""  """ 是多行注释 ,多行注释中可以任意使用 单双引号


#12 find 查找子字符串#
	find(...)
	    S.find(sub [,start [,end]]) -> int
	返回找到是
	
	>>> a="helloworld"
	>>> a.find("world")
	5
	>>> a.find("wo")  
	5
	>>> a.find("wo",5) 从第5个开始找
	5
	>>> a.find("wo",0,5) 在[0,5)中找不到
	-1


# 13 分割 #
	split(...)
	    S.split([sep [,maxsplit]]) -> list of strings
	   
	    Return a list of the words in the string S, using sep as the
	    delimiter string.  If maxsplit is given, at most maxsplit
	    splits are done. If sep is not specified or is None, any
	    whitespace string is a separator and empty strings are removed
	    from the result.

返回一个分割后的list
第二个参数指明分割次数


	>>> a="hello,world,haha"
	>>> print a.split(",")
	['hello', 'world', 'haha'] 
	>>> print a.split(",",1)  # 只允许分割一次
	['hello', 'world,haha']

