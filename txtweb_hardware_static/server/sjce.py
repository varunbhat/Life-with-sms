#!/usr/bin/env python
import cgi
from Databasing import Databasing
import cgitb; cgitb.enable()
print "Content-type: text/html\r\n"
xxx = {'txtWebId':'TEXT' , 'hash':'TEXT', 'verifyId':'TEXT', 'msg':'TEXT'}
form = cgi.FieldStorage()
deldb = form.getvalue('deletedb')
mydb = Databasing('sjce.db',xxx)
if deldb==1 or deldb=='1':
    mydb = Databasing('sjce.db',xxx,'w')
data  = mydb.read(-1,['msg'])

#for i in data:
#    print str(i[0])
    
