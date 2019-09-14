#coding:utf-8
people = 20
cats = 30
dogs = 15
#在python里面，如果一行以冒号结尾，那么它接下来的内容就应该缩进
if people < cats:
	print "people = %d, cats = %d, people < cats" % (people,cats)
if people > cats:
 	print  "people = %d, cats = %d, people > cats" % (people,cats)
if people < dogs:
 	print  "people = %d, dogs = %d, people < dogs" % (people,dogs)
if people >dogs:
 	print "people = %d, dogs = %d, people > dogs" % (people,dogs)
dogs += 5
if people >= dogs:
	print "people = %d, dogs = %d, people >= dogs" % (people,dogs)
if people <= dogs:
	print "people = %d, dogs = %d, people <= dogs" % (people,dogs)
if people == dogs:
	print "people = %d, dogs = %d, people == dogs" % (people,dogs)


