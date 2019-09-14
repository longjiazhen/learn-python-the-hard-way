#coding:utf-8
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def substract(a, b):
	print "SUBSTRACTING %d - %d" % (a, b)
	return a - b

def mutiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def devide(a, b):
	print "DEVIDING %d / %d" %(a, b)
	return a / b

print "Do some math"
A = add(5, 5)
B = substract(30, 20)
C = mutiply(2, 5)
D = devide(20, 2)
print "A = %d, B = %d, C = %d, D = %d" % (A, B, C, D)

#将一个函数的返回值作为另一个函数的参数
print "A puzzle"
X = add(A, substract(B, mutiply(C, devide(D, 2))))
#X=add(A, substract(B, mutiply(C, devide(10, 2))))
#X=add(A, substract(B, mutiply(10, 5)))
#X=add(A, substract(10, 50))
#X=add(10, -40 )
#X=-30
print "X = %d" % X

#自定义输入值，即：无论输入什么，都照本输出raw_input()
#将自定义输入值转换为整型int(raw_input())
#将自定义输入值转换为浮点型float(raw_input())
 
print "input data:"
origin_data = raw_input()
print "origin_data = %r" % origin_data
print "input data:"
int_data = int(raw_input())
print "int_data = %r" % int_data
print "input data:"
float_data = float(raw_input())
print "float_data = %r" % float_data
