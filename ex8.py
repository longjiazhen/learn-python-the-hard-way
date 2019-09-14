#coding:utf-8
formatter = "%r %r %r %r"
formatter2 = "%s %s %s %s"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight.")
#因为But it didn't sing里面有一个单引号，所以这一句是输出是用双引号，而其他的输出的单引号

print formatter2 % ("一", "二", "三", "四")
#使用%r的话，输出'\xe4\xb8\x80' '\xe4\xba\x8c' '\xe4\xb8\x89' '\xe5\x9b\x9b'
#所以想要输出中文的话，使用%s
#Q:为什么有时候明明用的是双引号，但是%r输出来的是单引号
#A:python会用最有效的方式来打印，而不会严格按照我们用的单引号还是双引号