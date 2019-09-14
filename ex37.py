#coding:utf-8
print "Which key words do you want to learn?"
print "A.del B.with and as"
select = raw_input("> ")
if select == "A":
	#del用法
	#python中del的用法不同于c的free和c++的delete
	#由于python都是引用，而python有gc机制，所以del语句作用在变量上，而不是数据对象上
	a = 1 #对象1被变量a引用，对象1的引用计数器为1
	b = a #对象1被变量b引用，对象1的引用计数器加1，为2
	c = a #对象1被变量c引用，对象1的引用计数器加1，为3
	del a #删除变量a，解除a对1的引用，对象1的引用计数器减1，为2
	del b #删除变量b，解除b对1的引用，对象1的引用计数器减1，为1
	print "c = %r" % c #输出1

	A = [1,2,3,4,5] #列表本身不包含数据，而是包含A[0] A[1] A[2] A[3] A[4]
	first = A[0] #拷贝列表，也不会有数据对象的复制，而是创建新的变量引用
	del A[0] 
	print "A = %r" % A #输出[2,3,4,5]
	print "first = %r" % first #输出1

elif select == "B":
	#with和as用法
	print "Here are 3 examples, which one would you like to learn?"
	select = raw_input("> ")
	if select == "1":
		#例如文件处理，首先获取一个文件句柄，从文件中读取数据，然后关闭文件句柄
		file = open("/Volumes/Transcend/py/test.txt")
		data = file.read()
		print "无异常处理",data
		file.close()
		#这里有2个问题，可能忘记关闭文件句柄，也可能文件读取数据异常，没有进行任何处理
		#加上异常处理
		file = open("/Volumes/Transcend/py/test.txt")
		try:
			data = file.read()
			print "比较冗长的异常处理",data
		finally:
			file.close()
		#但是代码比较冗长，如果用with as的话
		with open("/Volumes/Transcend/py/test.txt") as file:
			data = file.read()
			print "使用with as进行异常处理",data
	elif select == "2":
		#基本思想是，with所求值的对象必须有一个__enter__()方法和一个__exit__()方法
		#紧跟with后面的语句被求值以后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量
		#当with后面的代码块全部被执行完以后，将调用前面返回对象的__exit__()方法
		class Sample:
			"""docstring for Sample"""
			def __enter__(self):
				print "In __enter__()"
				return "Foo"
			def __exit__(self,type,value,trace):
				print "In __exit__()"
		def get_sample():
			return Sample()
		with get_sample() as sample:
			print "sample:",sample 
		#输出结果为：In __enter__()  sample: Foo  In __exit__()
		#可以看出，1）__enter__()方法被调用，
		#2）__enter__()方法返回的值Foo被赋值给变量sample，
		#3）执行with as的代码块，打印sample的值为Foo，
		#4）__exit__()方法被调用
	
	elif select == "3":
		#博客园链接 https://www.cnblogs.com/DswCnblog/p/6126588.html  看不懂
		#留意__exit__()函数的type，value，trace参数
		class Sample:
			def __enter__(self):
				return self
			def __exit__(self,type,value,trace):
				print "self:", self
				print "type:", type
				print "value:", value
				print "trace:", trace
			def do_something(self):
				bar = 1/0
				return bar + 10
			with Sample() as sample:
				sample.do_something()
	else:
		print "Please choose 1 or 2 or 3."
else:
	exit(0)




