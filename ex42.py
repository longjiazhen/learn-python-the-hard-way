#coding:utf-8
#Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object): #基类
	pass
#Dog is-a Animal
class Dog(Animal): #子类
	def __init__(self, name):
		#Dog has-a name
		self.name = name
#Cat is-a Animal
class Cat(Animal):
	def __init__(self, name):
		#Cat has-a name
		self.name = name
#Person is-a object  
class Person(object):
	def __init__(self, name):
		#Person has-a name and has-a pet
		self.name = name
		self.pet = None
#Employee is-a Person
class Employee(Person):
	def __init__(self, name, salary):
		#Employee has-a name
		super(Employee, self).__init__(name)
		#Employee has-a salary
		self.salary = salary
#Fish is-a object
class Fish(object):
	pass
#Salmon is-a Fish
class Salmon(Fish): #三文鱼
	pass
#Halibut is-a Fiash
class Halibut(Fish): #大比目鱼
	pass
#rover is-a Dog
rover = Dog("Rover")
#satan is-a Cat
satan = Cat("Satan")
#mary is-a Person
mary = Person("Mary")