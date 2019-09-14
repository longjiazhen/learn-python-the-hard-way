#coding:utf-8
tabby_cat = "\tI am tabbed in."
persian_cat = "I'm spilt\non a line."
backslash_cat = "I'm \\ a \\ cat."

#用"""和'''来输出多行字符串的效果是一样的
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip \n \t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


"""
while True:
	for i in['/', '-', '|', '\\', '|']:
		print "%s\r" % i,
"""


#这里用"""和'''来进行多行注释的效果是一样的
'''
\\ 输出反斜杠
\' 输出单引号
\" 输出双引号
\a 响铃符
\b 退格符
\f 进纸符
\n 换行符
\N{name} Unicode数据库中的字符名
\r ASCII 回车符
\t ASCII 水平制表符
\\uxxxx 值为16位十六进制值xxxx的字符 （其实只有一个反斜杠的哈）
\\Uxxxxxxxx 值为32位十六进制值xxxx的字符 （其实只有一个反斜杠的哈）
\v 垂直制表符
\\ooo 值为八进制值ooo的字符 （其实只有一个反斜杠的哈）
\\xhh 值为十六进制数hh的字符 （其实只有一个反斜杠的哈）
'''

