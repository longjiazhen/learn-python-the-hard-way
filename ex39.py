#coding:utf-8
import collections
#列表 --- 将下标（数字）作为元素的索引
print "Type 1 for tips, 2 for unsorted test, 3 for sorted test."
select = raw_input('> ')
if select == "1":
	things = ['a', 'b', 'c', 'd']
	print things[1] #b
	things[1] = 'z'
	print things[1] #z
	print things #['a','z','c','d']
	#字典 --- 可以将任意值（任意类型）作为元素的索引
	#字典的的key和value都是带单引号的（如果是字符串的话）
	#可以像列表一样读取任意位置的值，列表用thing[1]读取，字典用stuff['name']读取
	stuff = {
		'name' : "Zed",
		'age' : 36,
		'height' : 6*12+2
	}
	print stuff['name'] #Zed
	print stuff['age'] #36
	print stuff['height'] #74
	stuff['city'] = "San Francisco"
	print stuff['city'] #San Francisco
	#除了数字以外，还可以用字符串从stuff中获取元素，用字符串往stuff中添加元素
	stuff[1] = "Wow"
	stuff[2] = "Neato"
	print stuff[1] #Wow
	print stuff[2] #Neato
	print stuff #{'city': 'San Francisco', 2: 'Neato', 'name': 'Zed', 1: 'Wow', 'age': 36, 'height': 74}
	#删除字典中的元素
	del stuff['city']
	del stuff[1]
	del stuff[2]
	print stuff
elif select == "2":
	class Song(object):
			def __init__(self, lyrics):
				self.lyrics = lyrics
			def sing_me_a_song(self):
				for line in self.lyrics:
					print line
	happy_bday = Song(["Happy birthday to you",
                	"I don't want to get sued",
                   	"So I'll stop right there"])
	bulls_on_parade = Song(["They rally around the family",
					"With pockets full of shells"])
	happy_bday.sing_me_a_song()
	bulls_on_parade.sing_me_a_song()
else:
	#字典是无序的，collections.OrderedDict是有序的，是按输入顺序排列，而不是
	print "Regular dictionary"
	d = {}
	d['a'] = 'A'
	d['b'] = 'B' 
	d['c'] = 'C'
	for k,v in d.items():
		print "%s %s" %(k,v)
	print "Order dictionary"
	d1 = collections.OrderedDict()
	d1['c'] = 'C'
	d1['b'] = 'B'
	d1['a'] = 'A'
	for k,v in d1.items():
		print "%s %s" %(k,v)
	if d == d1:
		print "d == d1"
	else:
		print "d != d1"
	d2 = collections.OrderedDict()
	d2['a'] = 'A'
	d2['b'] = 'B' 
	d2['c'] = 'C'
	if d1 == d2:
		print "d1 == d2"
	else:
		print "d1 != d2"

			