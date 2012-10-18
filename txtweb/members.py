#!/usr/bin/env python
import urllib
import urllib2
import cgi
import sqlite3 as lite
import cgitb;
cgitb.enable()

print "Content-type: text/html\r\n\r\n"

class Donor:
#    def __init__(self,usn,weight,txtwbMob,mob):
#        self.usn =      usn
#        self.weight =   weight
#        self.txtwbMob = txtwbMob
#        self.mob =      mob

    def read(self):
        con = lite.connect('Donor.db')
        with con:    
            cur = con.cursor()    
            cur.execute("SELECT * FROM Donors")
            rows = cur.fetchall()
        for row in rows:
            print row  
            print "<br>"
            
            
myDon = Donor()
print '<p>'
myDon.read()
print '</p>'