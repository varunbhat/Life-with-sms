#!/usr/bin/env python
import sqlite3 as lite

#import cgi
#
#form = cgi.FieldStorage()
#keywords = form.getvalue('msg')
#
#keywords = keywords.split(' ')
#print keywords

def isAlpha(dat):
    try:
        x = int(dat)
        return False
    except:
        return True
    
x = ['asdfa',1344,'asdfadfa',534,2324,1243]
v = x.index(534)
print v
print x
print x[0:4]

