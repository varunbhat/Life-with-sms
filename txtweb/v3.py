#!/usr/bin/env python
import urllib
import urllib2
import cookielib
import cgi
import sqlite3 as lite
import sys
from urllib import urlopen


#http://blood4reva.tk/cgi-bin/divide/v4.py?txtweb-message=1re09ec101%2089%208050636905&txtweb-mobile=d71508a6-54db-484b-ba02-5628f4924cf9
servicetag = '07093fda-d254-4e77-a2bc-c3dc74a63baa'
form = cgi.FieldStorage()
hash = form.getvalue('txtweb-mobile')
userMsg = form.getvalue('txtweb-message')
verifyId = form.getvalue('txtweb-verifyid')
txtWebId = form.getvalue('txtweb-id')
alreadyRegd = 'alreadyRegd'
myMobile = "d71508a6-54db-484b-ba02-5628f4924cf9"
#myMobile = 'eafa06c4-4f54-42bb-8de9-2d4d1066ef48'
#myMobile = 'd1b3afb9-d524-4e16-a148-8e7de2fd4c70'
#mobs = ['405a0396-c56a-4d15-8a1b-1e58a943a2aa','3d3cc7a7-3655-4b09-bcd3-0534db6a4b3d','d1b3afb9-d524-4e16-a148-8e7de2fd4c70','eafa06c4-4f54-42bb-8de9-2d4d1066ef48'] 
pubId = "dd29f986-9a8b-4252-8bc8-f319644932b2"
errMsg = """Hey!! We did not receive the correct format.<br>
Please send:<br>
@blood4reva Full Name<br>
ex:<br>
@bloodforreva 1re09ec088 45 9999900000<br>
U can also register through the website www.bloodforreva.tk<br>
For any clarifications or doubts, reply<br>
@bloodforreva doubt Your-doubt<br>
We appretiate your participation.
"""
successMsg = 'Thank you for Registering'
print "Content-type: text/html"
print
print


def printHead():
    myHeader = """<html>
        <head>
            <title> Hello! </title>
            <meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
            <meta name='txtweb-appkey' content='""" + servicetag + """' />
        </head>
            <body>"""
def printTail():
    myTail = """</body>
    <html>"""
print myHeader

class Donor:
    def __init__(self, usn=None, weight=None, txtwbMob=None, mob=None):
        self.usn = usn
        self.weight = weight
        self.txtwbMob = txtwbMob
        self.mob = mob
    def write(self):
        try:
            con = lite.connect('Donor.db')
            with con:
                cur = con.cursor()    
                cur.execute("CREATE TABLE IF NOT EXISTS Donors(Id INTEGER PRIMARY KEY AUTOINCREMENT, USN TEXT, Weight INT, txtWbMobile TEXT,Mobile TEXT)")
    #            cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)
                cur.execute("SELECT * FROM Donors")
                rows = cur.fetchall()
                for row in rows:
                    if self.usn in row[1]:
                        return 3
                cur.execute("INSERT INTO Donors(USN,Weight,txtWbMobile,Mobile) VALUES (?,?,?,?)", (self.usn, self.weight, self.txtwbMob, self.mob))
                return 0
        except:
#            print "error"
            pass
    def read(self):
        con = lite.connect('Donor.db')
        with con:    
            cur = con.cursor()    
            cur.execute("SELECT * FROM Donors")
            rows = cur.fetchall()
#        for row in rows:
#            print row  
#            print "<br>"

                 
    def deleteDB(self):
        con = lite.connect('Donor.db')
        with con:    
            cur = con.cursor()   
            cur.execute("DROP TABLE IF EXISTS Donors")

class Push :
    import urllib2
    import urllib
    
    def __init__(self, pushNo="", pushData=""):
        self.pushHeader = """<html><head><title> Hello! </title><meta http-equiv='Content-Type' content='text/html; charset=UTF-8' /><meta name='txtweb-appkey' content='415224ee-da8f-46ba-a962-ed24760371af' /></head><body>"""
        self.pushTail = """</body></html>"""
        self.pubId = "dd29f986-9a8b-4252-8bc8-f319644932b2"
        self.pushNo = pushNo
        self.pushData = pushData    
    def data(self, dat):
        self.pushData = dat
    def send(self):
        if(self.pushData == "" or self.pushNo == ""):
            print "Push data requirements not satisfied"
        else:
            mydat = self.pushHeader + self.pushData + self.pushTail
            mydat = urllib.quote_plus(mydat)
            opener = urllib2.build_opener(urllib2.HTTPBasicAuthHandler())
            f = opener.open('http://api.txtweb.com/v1/push', 'txtweb-mobile=' + str(self.pushNo) + '&txtweb-message=' + mydat + '&txtweb-pubkey=' + pubId)
            dat = f.read()
            print dat
#            if "message>success</message>" in dat:
#                print 'sent'
#                pass

#push notification format
#reminder = Push(myMobile,"hello Mr Gay!!")
#reminder.send()



def insert(usn, age, hash, mobile, delx=0):
    myDon = Donor(usn, age, hash, mobile)
    if delx == 1:
        myDon.deleteDB()
    doneCode = myDon.write()
    if doneCode == 3:
        print alreadyRegd
        return 1


def isAlpha(dat):
    try:
        x = int(dat)
        return False
    except:
        return True

def validateUSN(myusn):
    f = urlopen('http://www.vtualerts.com/results/get_res.php?usn=' + myusn + '&sem=3')
    dat = f.read()
def validate():
    usn = ''
    weight = 0
    hashx = ''
    mobileNo = ''
    name = []
    startflag = -1
    if userMsg == None:
        print errMsg
        return
    else:
        keywords = userMsg.split(' ')
        for i in range(len(keywords)):
            if isAlpha(keywords[i]):
                keywords[i] = keywords[i].upper()
                if '1RE' in keywords[i]:
                    usn = keywords[i]
                    validateUSN(usn)
#                    print "USN "+ usn + '<br>'
                elif startflag == -1 or startflag == 0:
                    name.append(keyword[i])
                    startflag = 0
            if not(isAlpha(keywords[i])):
                if startflag == 0:
                    startflag = 1
#                if int(keywords[i])<150:    
#                    weight =int(keywords[i])
#                    print "Weight "+ str(weight) + '<br>'
#                else:
                if(int(keywords[i]) % 7000000000 > 0):
                    mobileNo = str(keywords[i])
#                    print "Mobile "+ mobileNo + '<br>'
        if ((not(usn == '' and name == []))  or mobileNo == ''):
            print errMsg
            return
    if not insert(usn, weight, hash, mobileNo):
        print 
#print userMsg
#userMsg = ' 1re09ec101  80 8050636905'
validate()
#for i in mobs:
#    reminder = Push(i,"Hello Everybody, This is varun. I'm testing the web app and i need your help. If u receive this sms please test me back at 8050636905. Thank you for the support. Take care")
#    reminder.send()

#
#def validate2():
#    if 
#    
validate2()
print myTail
