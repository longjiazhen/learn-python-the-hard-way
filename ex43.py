#coding:utf-8
#函数也可以作为一个变量
#cities['_find'] = find_city
#city_found = cities['_find'](cities, state)
#从后往前读代码
"""
1.cities和state是参数，传递给cities['_find']这个函数
2.citits是一个字典，key值_find对应的value是find_city
3.于是将find_city赋值给city_found
"""

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {  #phrases 词组
	"class ###(###)" : 
	 "Make a class named ### that is-a ###.",
	"class ###(object):\n\tdef __init__(self, ***)" :
	 "class ### has-a __init__ that takes self and *** parameters.",
	"class ###(object):\n\tdef ***(self, @@@)" :
	 "class ### has-a *** that takes self and @@@ parameters.",
	"*** = ###()" :
	 "set *** to an instance of class ###.",
	"***.***(@@@)" :
	 "from *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'" :
	 "from *** get the *** attribute and set it to '***'."
}

#do they want to drill phrases first
PHRASES_FIRST = False
if len(sys.argv)==2 and sys.argv[1]=="english" :
	print "111"
	PHRASES_FIRST = True

#load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip()) #strip()移除字符串头尾

def convert(snippet, phrase): #snippet 片段
	class_names = [w.capitalize() for w in #capitalize 大写
					random.sample(WORDS, snippet.count("###"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	result = []
	param_names = []

	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1, 3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))

	for sentence in snippet, phrase:
		result = sentence[:]

		#fake class names  #fake 伪造的
		for word in class_names:
			result = result.replace("###", word, 1)

		#fake other name
		for word in other_names:
			result = result.replace("***", word, 1)

		#fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)

		results.append(result)

	return results

#keep going until they hit ctrl-D
try:
	while True:
		snippets = (list(PHRASES.keys())[:])
		random.suffle(snippets) #shuffle()将序列的所有元素随机排序
		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASES_FIRST:
				question, answer = answer, question
			print question
			raw_input("> ")
			print "ANSWER: %s\n\n" % answer 
except EOFError:
	print "\nBye"


