#coding:utf-8
age = raw_input ("How old are you?"),
height = raw_input("How tall are you?"),
weight = raw_input("How much do you weigh?"),
#如果这上面的raw_input后面带上逗号的话，name输出是：
#So, you are ('35',) old, ('6\'22"',) tall and ('180lbs',) heavy.
#如果这上面的raw_input后面没有带上逗号，如上，那么符合预期结果，输出：
#So, you are '35' old, '6\'22"' tall and '180lbs' heavy.

print "So, you are %r old, %r tall and %r heavy." %(
	age, height, weight)

#在mac下，使用pydoc来查看帮助文档，pydoc raw_input，进入帮助文档页面以后，输出q退出
#