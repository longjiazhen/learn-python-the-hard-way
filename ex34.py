#coding:utf-8
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
print "%r" % animals
def jishu(i):
	print "The animal at %d is the %dst animal and is a %s." % (i,i+1,animals[i])
def xushu(i):
	print "The %dst animal is at %d and is a %s." % (i,i-1,animals[i-1])
#1. The animal at 1. 
jishu(1)
#2. The 3rd animal. 
xushu(3)
#3. The 1st animal. 
xushu(1)
#4. The animal at 3. 
jishu(3)
#5. The 5th animal. 
xushu(5)
#6. The animal at 2. 
jishu(2)
#7. The 6th animal. 
xushu(6)
#8. The animal at 4.
xushu(4)
#The 1st animal is at 0 and is a bear.
#The animal at 0 is the 1st animal and is a bear.