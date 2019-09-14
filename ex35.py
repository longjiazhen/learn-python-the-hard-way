#coding:utf-8
from sys import exit

def gold_room():
	print "This room is full of gold, how much do you want to take?"
	next = raw_input("> ")
	#if "0" in next or "1" in next:
	#用str.isdigit()来判断str是不是一个数值
	if next.isdigit():
	#python 2.x 用的都是raw_input，随便输入都是字符串
	#python 3用的是input，需要带引号才是字符串
		how_much = int(next)
	else:
		dead("Man,learn to type a number.")
	if how_much < 50:
		print "Well, you're not greedy, you win!"
		#exit(0)表示程序正常退出，1和其他数值均表示异常退出
		exit(0)
	else:
		dead("You're too greedy.")

def bear_room():
	print "There is a bear here."
	print "The bear has a banch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	print "Please type 'take honey' or 'taunt bear' or 'open door'"
	bear_moved = False
	while True:
		next = raw_input("> ")
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and bear_moved == False: #and not bear_moved
			print "The bear has moved from the door. You can go through it now. Plese choose again."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I don't know."

def cthulhu_room():
	print "Here you see the great evil Cthulhu." 
	print "Hey, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	next = raw_input("> ")
	if "flee" in next:
		start()
	elif "head" in next:
		print "Well that\'s tasty!"
	else:
		cthulhu_room()

def dead(why):
	print "%s good job!" % why
	exit(0)

def start():
	print "You are in a dark room."
	print "there is a door to your right and left."
	print "Which one do you take?"
	next = raw_input("> ")
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

start()





