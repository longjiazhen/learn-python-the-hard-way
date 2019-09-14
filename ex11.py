#coding:utf-8
#print语句的后面有逗号的话，输出这句话以后就不会换行，而是在同一行等待输入
#print语句的后面没有逗号的话，输出以后就会换行，到下一行去等待输入

print "How old are you?",
age = raw_input()
age11 = raw_input("How old are you??\n")
#这样输入How tall are you? 6'22"
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So,you are %r old, %r tall and %r heavy." % (age, height, weight)
#然后输出的结果So,you are '35' old, '6\'22"' tall and '180lbs' heavy.
#注意'6\'22"'这里，6'22"，自动在6后面的单引号前面加转义字符，避免将这认为是字符串的结束标志

#python 2.x用的是raw_input，随便输入都是字符串
#所以这里可以输入 zhangsan 7
name_raw = raw_input('输入姓名：')
age_raw = raw_input('输入年龄：')

#python 3用的是input，是字符串就得加上''
#这里要输入 'zhangsan' 7
name_in = input('输入姓名（要加引号）：')
age_in = input('输入年龄：')

#使用raw_input，将输入的字符串转换成数字
print "输入x:",
x = int(raw_input())
print "输入y:",
y = int(raw_input())
print "x + y = %d " % (x + y)



