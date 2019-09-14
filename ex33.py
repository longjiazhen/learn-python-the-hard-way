#coding:utf-8
'''
i = 0
numbers = [] 

while i < 6:
	print "At the top i is %d" % i 
	#append()向列表的尾部添加一个值
	numbers.append(i)
	i += 1
	print "Numbers now: %r" % numbers
	print "At the bottom i is %d" % i

print "The numbers:"
for num in numbers:
	print num
'''
'''
def while_loop(count,lag):
	i = 0
	numbers = []
	while i < count:
		print "At the top i is %d" % i
		numbers.append(i)
		i += lag
		print "Numbers now: %r" % numbers
		print "At the bottom i is %d" % i
	print "The numbers:"
	for num in numbers:
		print num
while_loop(10,2)
'''
A = []
for i in range(0,10,2):
	A.append(i)
print "A = %r" % A
