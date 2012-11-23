#!/usr/bin/env python
import urllib
import urllib2
import cookielib
import cgi
import sqlite3 as lite
import sys

form = cgi.FieldStorage()
mobile = form.getvalue('txtweb-mobile')
userMsg = form.getvalue('txtweb-message')
verifyId = form.getvalue('txtweb-verifyid')
txtWebId = form.getvalue('txtweb-id')
myMobile = "d71508a6-54db-484b-ba02-5628f4924cf9"
pubId = "dd29f986-9a8b-4252-8bc8-f319644932b2"
print "Content-type: text/html"
print
       
myHeader = """<html>
    <head>
        <title> Hello! </title>
        <meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
        <meta name='txtweb-appkey' content='415224ee-da8f-46ba-a962-ed24760371af' />
    </head>
        <body>"""
myTail = """</body>
    <html>"""
print myHeader

class Donor:
    def __init__(self,usn,weight,txtwbMob,mob):
        self.usn =      usn
        self.weight =   weight
        self.txtwbMob = txtwbMob
        self.mob =      mob
    def write(self):
        con = lite.connect('Donor.db')
        with con:
            cur = con.cursor()    

            cur.execute("CREATE TABLE IF NOT EXISTS Donors(Id INTEGER PRIMARY KEY AUTOINCREMENT, USN TEXT, Weight INT, txtWbMobile TEXT,Mobile TEXT)")
#            cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)
            cur.execute("INSERT INTO Donors(USN,Weight,txtWbMobile,Mobile) VALUES (?,?,?,?)",(self.usn,self.weight,self.txtwbMob,self.mob))
    def read(self):
        con = lite.connect('Donor.db')
        with con:    
            cur = con.cursor()    
            cur.execute("SELECT * FROM Donors")
            rows = cur.fetchall()

        for row in rows:
            print row [1] 
            print "<br>"          
    def deleteDB(self):
        con = lite.connect('Donor.db')
        with con:    
            cur = con.cursor()   
            cur.execute("DROP TABLE Donors")

class Push :
    import urllib2
    import urllib
    
    def __init__(self,pushNo = "",pushData= ""):
        self.pushHeader = """<html><head><title> Hello! </title><meta http-equiv='Content-Type' content='text/html; charset=UTF-8' /><meta name='txtweb-appkey' content='415224ee-da8f-46ba-a962-ed24760371af' /></head><body>"""
        self.pushTail = """</body></html>"""
        self.pubId = "dd29f986-9a8b-4252-8bc8-f319644932b2"
        self.pushNo = pushNo
        self.pushData = pushData    
    def data(self,dat):
        self.pushData = dat
    def send(self):
        if(self.pushData=="" or self.pushNo==""):
            assert "Push data requirements not satisfied"
        else:
            mydat = self.pushHeader + self.pushData + self.pushTail
            mydat = urllib.quote_plus(mydat)
            opener = urllib2.build_opener(urllib2.HTTPBasicAuthHandler())
            f = opener.open('http://api.txtweb.com/v1/push', 'txtweb-mobile=' + str(self.pushNo) +  '&txtweb-message='+mydat+'&txtweb-pubkey='+pubId)
            dat = f.read()
            if "message>success</message>" in dat:
                pass

#/////////////////////////////////////////////////
#push notification format
#reminder = Push(myMobile,"Hello")
#reminder.send()
#/////////////////////////////////////////////////

if True:
    print '<p>'
    print "hello"
#///////////////////////////////////////////////////////
#    myDon = Donor('1re09ec101',69,myMobile,'8050636905')
#    myDon.write()
#    myDon.read()
#myDon.deleteDB()
#///////////////////////////////////////////////////////
    print '</p>'


print myTail
