#coding:utf-8
#append()函数其实是需要2个参数的，默认第一个参数是调用append()的那个变量本身
#mystuff.append('Hello') = mystuff.append(mystuff,'Hello')
#create a mapping of state to abbreviation缩写
states = {
	'Oregon' : 'OR',
	'Florida' : 'FL',
	'California' : 'CA',
	'New York' : 'NY',
	'Michigan' : 'MI'
}
#create a basic set of states and some cities in them
cities = {
	'CA' : 'San Francisco',
	'MI' : 'Detroit',
	'FL' : 'Jacksonville'
}
#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
#print out some cities
print '-' * 10 #打印 -----------
print "NY States has: ", cities['NY']
print "OR States has: ", cities['OR']
#print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']
#do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ",cities[states['Florida']]
#print every state abbreviation
print '-' * 10
#Dict = {A:a, B:b, C:c}这种叫字典，前面是key，后面是value
#可用items()方法返回遍历的(key, value)列表
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)
#print every city in state
print '-' * 10
for key, value in cities.items():
	print "%s has city %s" % (key, value)
#now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)
	print "%s has city %s" % (abbrev, cities[abbrev]) #???这里为什么不是'abbrev'
#safely get a abbreviation by state that might not be there
print '-' * 10
#可用get()方法从字典中获取指定key值对应的value，若无此key值则返回None
#Dict.get(key[,default None]) 
#第二个参数可以不填，可以填None，也可以填任意字符串
#state = states.get('Texas', None)
state = states.get('Texas')
if not state:
	print "Sorry, no Texas."
#get a city with a default value
print '-' * 10
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is %s" % city
