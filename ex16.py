#coding:utf-8
from sys import argv

script, filename = argv

print "We are going to earse %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, do hit RETURN."

raw_input("? ")
print "Opening the  file..."
target = open(filename, 'w')
#target = open(filename) #这样默认打开时只有读权限'r'

print "Truncating the file. Goodbye!"
target.truncate() #清空文件


print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these into the file."

"""
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
"""

tmp = line1 + "\n" + line2 + "\n" + line3 + "\n"
target.write(tmp)

print "And finally, we close it."
target.close()

print "Here's your file."
target = open(filename, 'r')
print target.read()
target.close()

#打开文件的方式：
#w：write写；
#r：read读；
#a：append追加；
#w+，r+，a+：同时以读写方式打开

