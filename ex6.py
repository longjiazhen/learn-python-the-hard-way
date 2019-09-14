#coding:utf-8
#百分号后面可以直接跟数值，表示输出这个数字
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#百分号后面也可以跟变量，表示输出这个变量的值
#跟多个变量的话，用括号把这些变量括起来
y = "Those who knows %s and those who %s" % (binary, do_not)

print x #这样输出的是不带引号的
print y

#百分号后面跟单个变量
#%r表示后面无论是什么，都直接输出来
print 'I said1' #这样输出不带引号
print "I said2" #这样输出不带引号，这里单引号和双引号都是一样的，不区分
print 'I said1: %r.' % x #这样输出的x带单引号 
print "I said2: %r." % x #这样输出的x带单引号 ---- 其实就是上面说的输出不区分单引号和双引号

print "I also said1: '%r'." % y #这样输出的y是单引号里面带双引号，因为对%r用了单引号，而y本身就有双引号
print 'I also said2: "%r".' % y #这样输出的y是双引号里面带双引号，因为对%r用了双引号，而y本身就有双引号
print "I also said3: '%s'." % y #这样输出的y带单引号，使用%s的意思是，只输出y里面的内容，不输出y本身带的那个双引号
print 'I also said4: "%s".' % y #这样输出的y带双引号，上一句是单引号，因为'%s'，这一句是双引号，因为"%s"




hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#所以这个地方，一个字符串%另一个字符串，用来将两个字符串连在一起输出，实现的效果跟下面的加号差不多
#意思是，上面hilarious赋值为False还是True并不重要，重要的是，joke_evaluation的后面要有%r
print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string of a right side."
#可以用加号连接两个字符串
print w + e

#%r用来做调试比较好，因为它可以显示原始数据，而其他%s，%d都是用来向用户输出的

