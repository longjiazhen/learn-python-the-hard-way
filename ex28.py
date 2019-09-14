#coding:utf-8
"""
print "Start testing:"
A = True and True
print "True and True: T %r" % A
A = False and True
print "False and True: F %r" % A
A = 1==1 and 2==1
print "1==1 and 2==1: F %r" % A
A = "test" == "test"
print '"test" == "test": T %r' % A
A = 1==1 or 2!=1
print "1==1 or 2!=1: T %r" % A
A = True and 1==1
print "True and 1==1: T %r" % A
A = False and 0!=0
print "False and 0!=0: F %r" % A
A = True or 1==1
print "True or 1==1: T %r" % A
A = "test" == "testing"
print ' "test" == "testing": F %r' % A
A = 1!=0 and 2==1
print "1!=0 and 2==1: F %r" % A
A = "test" != "testing"
print 'test" != "testing": T %r' % A
A = "test" == 1
print '"test" == 1: F %r' % A
A = not (True and False)
print "not (True and False): T %r" % A
A = not (1==1 and 0!=1)
print "not (1==1 and 0!=1): F %r" % A
A = not (10==1 or 1000==1000)
print "not (10==1 or 1000==1000): T %r" % A
A = not(1!=10 or 3==4)
print "not(1!=10 or 3==4): F %r" % A
A = not("testing"=="testing" and "Zed"=="Cool Guy")
print 'not("testing"=="testing" and "Zed"=="Cool Guy"): T %r' % A
A = 1==1 and not ("testing"==1 or 1==0)
print '1==1 and not ("testing"==1 or 1==0): T %r' % A
A = "trunky"=="bacon" and not (3==4 or 3==3)
print 'trunky"=="bacon" and not (3==4 or 3==3): F %r' % A
A = 3==3 and not ("testing"=="testing" or "Python"=="Fun")
print '3==3 and not ("testing"=="testing" or "Python"=="Fun"): F %r' % A
"""

A = "test" and "test"
print "test and test: test %r" % A
A = 1 and 1
print "1 and 1: 1 %r" % A
print "======="
A = False and 1
print "False and 1: False %r" % A
A = 1 and False
print "1 and False: False %r" % A
A = 0 and True
print "0 and True: 0 %r" % A
A = True and 0
print "True and 0: 0 %r" % A
A = 1 and True
print "1 and True: True %r" % A
A = True and 1
print "True and 1: 1 %r" % A
A = 0 and False
print "0 and False: 0 %r" % A
A = False and 0
print "False and 0: False %r" % A
print "--------"
A = False or 1
print "False or 1: 1 %r" % A
A = 1 or False
print "1 or False: 1 %r" % A
A = 0 or True
print "0 or True: True %r" % A
A = True or 0
print "True or 0: True %r" % A
A = 1 or True
print "1 or True: 1 %r" % A
A = True or 1
print "True or 1: True %r" % A
A = 0 or False
print "0 or False: False %r" % A
A = False or 0
print "False or 0: 0 %r" % A
