#coding:utf-8
def cheese_and_crackers(cheese_count, box_of_crackers):
	print "You have %d cheese." % cheese_count
	print "You have %d crackers." % box_of_crackers
	print "That's enough.\n"
"""
print "We just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR we can user variables from the script:"
amount_of_cheese = 40
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math"
cheese_and_crackers(amount_of_cheese+40, amount_of_crackers+50)
"""

a = int(raw_input("cheese numbers:"))
b = int(raw_input("crackers numbers:"))
cheese_and_crackers(a,b)
#使用int()把raw_input()的值转化为整数

"""
a = input("cheese numbers:")
b = input("crackers numbers:")
cheese_and_crackers(a,b)
"""




