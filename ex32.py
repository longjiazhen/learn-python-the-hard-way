#coding:utf-8
"""
the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'penies',2,'dimes',3,'quarters']

#用这种for循环来遍历一个列表
for number in the_count:
	print "This is count %d" % number

for fruit in fruits:
	print "A fruit of type: %s" % fruit

for i in change:
	#不知道列表中的内容是什么数据类型，可以使用%r
	print "I got %r" % i

#建立一个列表，首先建立一个空列表
elements = []
#for i in range(0,6)循环6次，含首不含尾，0-5
for i in range(0,6):
	print "Adding %d to the list" % i
	#append()函数表示在末尾添加
	elements.append(i)

#直接输出整个列表的内容
print "----"
elements = range(0,6)
print "%r" % elements
print "----"

#依次输出列表的每一项
for i in elements:
	print "Elemen was %d" % i
"""

#如果不填step，默认是1，若step=2，意思是0 2 4 6 8 这样循环
for i in range(0,10,2):
	print "i = %d" %i
#二元列表
A = [[1,2,3],[4,5,6]]
for i in range(0,2):
	for j in range(0,3):
		print "A[%d][%d] = %d" % (i,j,A[i][j])
		