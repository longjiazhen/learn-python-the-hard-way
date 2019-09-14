#coding:utf-8
#如果代码中出现中文，即使是中文注释，也要加上这一行coding:utf-8
#用pydoc查看帮助文档

from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

#rewind的中文意思是：倒回
def rewind(f):
	f.seek(0)
#file.seek()的意思是将游标移动到任意位置，然后在当前位置进行操作，0表示从头开始

def print_a_line(line_count, f):
	print line_count, f.readline(),
#readline()读到\n为止，所以的末尾本来就有\n
#print的末尾本来也有\n，所以下面会看到空行
#解决办法是：在print的后面加逗号，这样就不会输出换行符了

current_file = open(input_file)

print "First let's print the whole file:"
print_all(current_file)


#这个rewind的目的是回到开头
print "Now let's rewind, kinds of like a tape."
rewind(current_file)

#current_file只是一个变量（字符串），用来存储文件里的一些内容，它不是一份文件，不能调用seek()等函数
#current_file = current_file.seek(0)

print "Let's print 3 lines:"
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)

