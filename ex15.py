#coding:utf-8
from sys import argv
#sys是一个代码库，从sys中取出argv这个功能


script, filename = argv

txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()



#由用户输入文件名
script = argv
filename = raw_input("请输入文件名：")
txt = open(filename)

print "Here's your file:"
print txt.read()
txt.close()


#在命令行打开文件
#再次运行 python 在命令行下使用 open 打开一个文件，这种 open 和 read 的方法也值得你一学
#longjiazhendeMacBook-Air:py longjiazhen$ python 
#Python 2.7.10 (default, Feb 22 2019, 21:55:15) 
#[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin
#Type "help", "copyright", "credits" or "license" for more information.
#>>> print open("ex15_sample.txt").read()
#This is stuff I typed into file.
#It is really cool stuff.
#Lots and lots of fun to have here.
#>>> 