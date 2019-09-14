#coding:utf-8
class mystuff(object):
	def __init__(self):
		self.tangerine = "And now a thousand years between"
	def Apple(self):
		print "I AM CLASSY APPLES!"
thing = mystuff()
thing.Apple()
print thing.tangerine

print '='*10
class Song(object):
		def __init__(self, lyrics):
			#为什么要加self，为了明确是对象的lyrics属性，还是一个叫lyrics的局部变量
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



