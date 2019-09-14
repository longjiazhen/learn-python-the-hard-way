#coding:utf-8
#隐式继承
print "隐式继承"
class Parent(object):
	def implicit(self):
		print "PARENT implicit()"
class Child(Parent):
	pass
dad = Parent()
son = Child()
dad.implicit() #输出 PARENT implicit()
son.implicit() #输出 PARENT implicit()

#显式覆写
print "显式覆写"
class Parent(object):
	def override(self):
		print "PARENT override()"
class Child(Parent):
	def override(self):
		print "CHILD override()"
dad = Parent()
son = Child()
dad.override() #输出 PARENT override()
son.override() #输出 CHILD override()

#在运行前或者运行后覆写
print "在运行前或者运行后覆写"
class Parent(object):
	def altered(self):
		print "PARENT altered()"
class Child(Parent):
	def altered(self):
		print "CHILD, BEFORE PARENT altered()" #输出 CHILD, BEFORE PARENT altered()
		super(Child, self).altered() #输出 PARENT altered()
		print "CHILD, AFTER PARENT altered()" #输出 CHILD, AFTER PARENT altered()
dad = Parent()
son = Child()
dad.altered() #输出 PARENT altered()
son.altered() #调用super并且加上Child和self两个参数，在此返回的基础上然后调用altered()

#以上三种方式共用
print "以上三种方式共用"
class Parent(object):
	def override(self):
		print "PARENT override()"
	def implicit(self):
		print "PARENT implicit()"
	def altered(self):
		print "PARENT altered()"
class Child(Parent):
	def override(self):
		print "CHILD override()"
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"
dad = Parent()
son = Child()
dad.implicit() #PARENT implicit()
son.implicit() #PARENT implicit()
dad.override() #PARENT override()
son.override() #CHILD override()
dad.altered() #PARENT altered()
son.altered() #CHILD, BEFORE PARENT altered() PARENT altered() CHILD, AFTER PARENT altered()

#多重继承
print "多重继承"
#创建一个叫做SuperFun的类，让它同时继承Child和BadStuff
#class SuperFun(Child, BadStuff):
#	pass
#最常见的super的用法是在基类的__init__()中使用
class Child(Parent):
	def __init__(self, stuff):
		self.stuff = stuff
		super(Child, self).__init__()

#合成
print "合成"
class Other(object):
	def override(self):
		print "OTHER override()"
	def implicit(self):
		print "OTHER implicit()"
	def altered(self):
		print "OTHER altered()"
class Child(object):
	def __init__(self):
		self.other = Other()
	def implicit(self):
		self.other.implicit()
	def override(self):
		print "CHILD override()"
	def altered(self):
		print "CHILD, BEFROE OTHER altered()"
		self.other.altered()
		print "CHILD, AFTER OTHER altered()"
son = Child()
son.implicit() #OTHER implicit()
son.override() #CHILD override()
son.altered() #CHILD, BEFROE OTHER altered() OTHER altered() CHILD, AFTER OTHER altered()
#也就是说class Child(object):def __init__(self):self.other = Other() ==> class Child(Other)
#前面Child和Parent的关系是 A是B，而这里Child和Other的关系是 A里有B






