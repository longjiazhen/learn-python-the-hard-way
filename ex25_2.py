#coding:utf-8

def break_words(stuff):
	"""This function will break words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after poping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after poping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last word of a sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

"""
在python里面运行代码，运行完以后可以看到，同一文件夹下生成了一份文件ex25_2.pyc
运行方式如下：
1）在命令行输入python，进入到python里面，光标变成>>>
2）输入import ex25 注意这里不带.py
3）输入from ex25 import * 表示将ex25的所有内容导入进来
4）也可以不用3），不过那样的话，后面调用函数要用ex25.break_words()，而不能直接用break_words()
5）接下来就可以正常一步步地执行了，给变量赋值以后，再输一遍变量名，表示输出这个变量值
比如：>>> words = break_words(sentence) 然后 >>> words
”“”



