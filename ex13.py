#coding:utf-8
#写一个可接受参数的脚本
#将参数变量引入python
from sys import argv

#将argv中的东西解包，将变量依次赋予左边的变量名
script, first, second, third = argv

first = raw_input('第一个参数：')
second = raw_input('第二个参数：')
third = raw_input('第三个参数：')

#argv和raw_input的区别：
#argv是在运行的时候直接输入的，raw_input是在运行过程中输入的

print "The script is called:", script
print "You first variable is:", first
print "You second variable is:", second
print "You third variable is:", third