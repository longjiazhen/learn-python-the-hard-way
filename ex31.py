#coding:utf-8
#怎样判断一个数字属于某个阈值中：用1<x<10或者x in range(1,10)
print "You enter a dark room with two doors. Do you go throught door #1 or door #2?"
door = raw_input("> ")

if door == "1":
	print "There is a gaint bear eating a cake. What do you do?"
	print "1.Take the cake."
	print "2.Scream at the bear."

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats you face off."
	elif bear == "2":
		print "The bear eats you legs off."
	else:
		print "Well, doing %s is probably better, the bear run away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1.Bluebarries."
	print "2.Yellow jacket clothespines."
	print "3.Understanding resolvers yellow melodies."

	insanity = raw_input("> ")

	if insanity==1 or insanity==2:
		print "Your body survives powered by a mind of jello."
	else:
		print "The insanity rots your eyes into a pool of muck."

else:
	print "You stumble around and fall on a knife and die."
