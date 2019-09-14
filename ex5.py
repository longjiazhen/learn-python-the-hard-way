#coding:utf-8
name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74*2.54 #inches
# 1英寸 = 2.54cm
weight = 180*0.45 #lbs
# 1磅 = 0.45千克
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d cm tall." % height
print "He's %d kg heavy." % weight
print "Actutally that's not too heavy."
print "He's get %s eyes and %s hair." % (eyes,hair)
print "He's teeth are usually %s depending on the coffee." % teeth

#This line is tricky, try to get it exactly right.
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# %r 不论是什么都打印出来

# %% 输出一个百分号
# %c 字符及其ASCII码
# %s 字符串
# %d 有符号整数（十进制）
# %u 无符号整数（十进制）
# %o 无符号整数（八进制）
# %x 无符号整数（十六进制）
# %X 无符号整数（十六进制大写字母）
# %e 浮点数字（科学计数法）
# %E 浮点数字（科学计数法，用E代替e）
# %f 浮点数字（用小数点符号）
# %g 浮点数字（根据值的大小采用%e或者%f）
# %G 浮点数字（类似%g）
# %p 指针（用于十六进制打印值的内存地址）
# %n 存储输出字符的数量放进参数列表的下一个变量中

