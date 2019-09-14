#this one is like your script with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1:%r, arg2:%r" % (arg1, arg2)
#定义了函数以后，以冒号结尾，然后下面的函数内容需要缩进
#*argv里面的*的意思是：告诉python让它把函数的所有参数都接收进来，然后放到名字叫args的列表中去

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1:%r, arg2:%r" % (arg1, arg2)

#this just take one agrument
def print_one(arg1):
	print "arg1:%r" % arg1

#this take no argument
def print_none():
	print "I got nothing."

print_two("A1", "A2")
print_two_again("B1", "B2")
print_one("H")
print_none()

