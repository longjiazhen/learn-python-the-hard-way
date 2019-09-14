#coding:utf-8
#Here's some new strange stuff,remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days:",days
#%r是输出所有内容，所以\n不生效
print "Here are the months1: %r" % months
print "Here are the months2: %s" % months

#这是输出长字符串，其中可以包含换行等
print """
There are something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

#这是多行注释，差别在于，第一次三个省略号的前面有没有换行
"""
There are something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""