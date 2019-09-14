#coding:utf-8
people = 40
cars = 20
buses = 25

if cars > people:
	print "cars = %d, people = %d, cars > people" % (cars,people)
#不是else if，而是elif
elif cars != people:
	print "cars = %d, people = %d, cars != people" % (cars,people)
elif cars < people:
	print "cars = %d, people = %d, cars < people" % (cars,people)
else:
	print "cars = %d, people = %d, cars == people" % (cars,people)

if buses > cars:
	print "buses = %d, cars = %d, buses > cars" % (buses,cars)
elif buses < cars:
	print "buses = %d, cars = %d, buses < cars" % (buses,cars)
else:
	print "buses = %d, cars = %d, buses == cars" % (buses,cars)

if people > buses:
	print "people = %d, buses = %d, people > buses" % (people,buses)
else:
	print "people < buses or people == buses."
