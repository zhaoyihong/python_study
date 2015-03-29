 
#  异常 #

exception,中译异常，保守派的圣杯，被滥用的良药。


## 1.出错的东西们，他们出了什么错. ##


他们出错 = 被抛出了异常




## 2.我们不想让他们出错，该怎么办。 ##

exception来了。


## 3.基本语法 ##


## 4.我们为什么不让他出错？ ##

在开发阶段，我们是可以让任何东西出错的。


## 5.什么时候用，怎么用？ ##

  我们什么时候用异常？ 不得不用的时候。

  异常怎么用？

  	1.(我们知道会有哪些问题，分析问题，得到这些问题会抛出的指定异常)捕获正确的异常，不要直接 try except
  	2.异常的处理，要合理。要有日志。



a = [1,2,3,4,5,6]


print a[5]

try:
print a[6]
except:
print u"哈哈哈哈，这里出错啦"


print '继续往下跑哦'





try:
" 框住了你感觉会抛出异常的代码 "

print "41223123"

print a[6]

print "hahaha"

except:

" try代码块里的代码如果抛出异常了，该执行什么内容"

print u"哈哈"
else:

"try代码块里的代码如果没有跑出异常，就执行这里"

print "hoho"
finally:

"不管如何，finally里的代码，是总会执行的"

print "xixi"





import urllib


sth_url = "http://wasdasdasd"


try:
d = urllib.urlopen(sth_url)
except IOError:
print "哈哈哈出错了"
except 语法错误的异常:
print 
else:
content = d.read()
finally:
d.close()