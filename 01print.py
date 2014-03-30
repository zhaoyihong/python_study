#!/usr/bin/python
# coding=utf-8
'''
	print 用来打印整形 浮点型 字符串
'''
print 2
print 12.5
print 'H'
print 'wwww.baidu.com'
x=12
print x
y=12.8
print y
#打印多个变量
print x,y
#格式化输出  print(format(var,format_modifier))
#6.3f : 输出占6位,小数点后三位 
#m.n  m总位数 n小数位数
#实际小数位数小于n,则右边0补齐
#若位数小于m,会在左边补齐空格,做右对齐
print format(12.34567,'6.2f') # 12.35
print format(12.34567,'6.3f')  #12.346
print format(12.34567,'6.9f') #12.345670000 
print format(12.34567,'6.0f') #    12

#打印百分数 m.n% m,n的意思和上面一样
print format(0.3456,'.2%') #34.6
print format(0.3456,'6.1%') # 34.6%

