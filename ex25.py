#coding:utf-8

def break_words(stuff):
	"""This function will break words for us."""
	words = stuff.split(' ') #按空格来分割
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after poping it off."""
	word = words.pop(0)  #pop(0)表示第一个
	print word

def print_last_word(words):
	"""Prints the last word after poping it off."""
	word = words.pop(-1)  #pop(-1)表示最后一个
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

#下面两个函数可以直接运行，不需要赋值给某个变量是因为：
#print_first_word和print_last_word这两个函数都没有返回值，最后一句是print而不是return
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
sentence = "All goods come to those who wait."
#words = break_words(sentence)
print "Print first and last:"
print_first_and_last(sentence)
print "Print first and last sorted:"
print_first_and_last_sorted(sentence)
"""
#这是正常在命令行运行.py的方式
#ex25_2.py是在python里面运行的方式


