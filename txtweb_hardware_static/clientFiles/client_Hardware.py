#!/usr/bin/env python
import cgi
from Databasing import Databasing
import os,time
import serial 
#import cgitb; cgitb.enable()

print "Content-type: text/html\r\n\r\n"

f = open("finishedcmds.txt",'a')
while 1:
#    os.system("wget http://geek-tronics.com/cgi-bin/txtweb/sjce.db")
    os.system("GET http://geek-tronics.com/cgi-bin/txtweb/sjce.py > databaselist.txt")
    
    PORT = 0
    BAUD = 9600
    
    f = open('databaselist.txt')
    zsd = f.read()
    zsd = zsd.split('\n')
    
    
    ser = serial.Serial('/dev/ttyACM'+str(PORT), BAUD,timeout=1)
    xxx = {'txtWebId':'TEXT' , 'hash':'TEXT', 'verifyId':'TEXT', 'msg':'TEXT'}
    form = cgi.FieldStorage()
    deldb = form.getvalue('deletedb')
    mydb = Databasing('sjce.db',xxx)
    if deldb==1 or deldb=='1':
        mydb = Databasing('sjce.db',xxx,'w')
    data  = mydb.read(-1,['msg'])
    for i in zsd:
        if i == '':
            continue
        if 'on' in i:
            ser.write(1)
        else :
            ser.write(0)
        time.sleep(5)
        print i

