 
正则表达式，是字符串检索引擎，最早起源于unix。

## 1.unix下的正则 awk grep egrep ##


## 2.正则的几个基本概念 ##
	
	[0-9] 
	\d 全部数字   
	\D非数字 
	\s空格
	\S 非空格
	\w 单词类字符 a-z A-Z 0-9 _
	\W 非单词类字符
	[a-zA-Z] 字母

	. 任意字符
	
	+ 前面的表达式，出现1到无限次  最少，出现1次
	? 前面的表达式，出现0到1次  最多，出现1次
	* 前面的表达式，出现0到无限次 出现不出现，都没关系
	
	{2}  {n}  前面的表达式匹配n次
	{0,2} {m,n} 前面的表达式匹配m到n次


![](http://i.imgur.com/Et6l6jt.png)

更多请见：[http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html](http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html)

	
## 3.python里的正则模块 re ##



## 4.一些基本操作 ##


### 4.1 从头取配 match  ###

re.match函数

	match(pattern, string, flags=0)
    Try to apply the pattern at the start of the string, returning
    a match object, or None if no match was found.

注意match函数是从字符串头开始的，在开头找到匹配就返回一个match object，找不到就返回None

re.groups  用来获取正则中被括号括起来的匹配值的元组

re.group(num) 用来获取第num个被匹配到的值

示例：
	
	>>> print re.match('(\w+) +(\w+)','hello world').groups() 
	('hello', 'world')


### 4.2 切割 split ###

	>>> e = "a1b2c3d4"
	>>> re.split('\d',e)
	['a', 'b', 'c', 'd', '']
	>>> re.split('\D',e)
	['', '1', '2', '3', '4']

### 4.3 search 寻找一个 ###

	re.search
	
	Help on function search in module re:
	
	search(pattern, string, flags=0)
	    Scan through string looking for a match to the pattern, returning
	    a match object, or None if no match was found.

search函数从头开始搜索字符串，找到第一个匹配

	>>> a  = re.search('\d+',"a123bc234") 
	>>> print a.group()                   
	123


### 4.4 查找全部 findall ###

findall 找到所有正则条件的表达式，并输出的到list中返回

	
	>>> re.findall('<.*?>','<100><200>')
	['<100>', '<200>']
	
	其中的？是非贪婪模式的意思


### 4.5 替换 ###

 
	sub(pattern, repl, string, count=0, flags=0)
	    Return the string obtained by replacing the leftmost
	    non-overlapping occurrences of the pattern in string by the
	    replacement repl.  repl can be either a string or a callable;
	    if a string, backslash escapes in it are processed.  If it is
	    a callable, it's passed the match object and must return
	    a replacement string to be used.


返回的字符串是在字符串中用 RE 最左边不重叠的匹配来替换。如果模式没有发现，字符将被没有改变地返回。


	>>> a=re.sub("#.*$","","010-123-45#this is the phone number")
	>>> a
	'010-123-45'
	>>> a=re.sub('\D','',a)
	>>> a
	'01012345'


默认是替换所有，可以在count参数中设置替换的个数



### 4.6 finditer 迭代器什么的最有爱了 ###

和findall的功能差不多，查找所有的匹配

但是findall返回一个列表。finditer返回迭代器。



	s = "111 222 333 444 555"
	for i in re.finditer('\d+',s):
	    print i.group(),i.span()


	结果：

	111 (0, 3)
	222 (4, 7)
	333 (8, 11)
	444 (12, 15)
	555 (16, 19)



### 4.7 标识 ###

	re.I	使匹配对大小写不敏感
	re.L	做本地化识别（locale-aware）匹配
	re.M	多行匹配，影响 ^ 和 $
	re.S	使 . 匹配包括换行在内的所有字符
	re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
	re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。