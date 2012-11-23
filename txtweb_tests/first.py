#!/usr/bin/env python
import urllib
import urllib2, cookielib
import cgi


form = cgi.FieldStorage()
mobile = form.getvalue('txtweb-mobile')
userMsg = form.getvalue('txtweb-message')
verifyId = form.getvalue('txtweb-verifyid')
txtWebId = form.getvalue('txtweb-id')
print "Content-Type: text/html"
print
       
myHeader = """<html>
    <head>
        <title> Hello! </title>
        <meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
       <!-- <meta name='txtweb-appkey' content='415224ee-da8f-46ba-a962-ed24760371af' />-->
    </head>
        <body>"""
myTail = """</body>
    <html>"""
print myHeader
 
myMobile = "d71508a6-54db-484b-ba02-5628f4924cf9"
pubId = "dd29f986-9a8b-4252-8bc8-f319644932b2"
##print "Content-type:text/html\r\n\r\n"


class Push :
    import urllib2
    import urllib
    
    def __init__(self,pushNo = "",pushData= ""):
        self.pushHeader = """<html><head><title> Blood for Reva </title><meta http-equiv='Content-Type' content='text/html; charset=UTF-8' /><meta name='txtweb-appkey' content='415224ee-da8f-46ba-a962-ed24760371af' /></head><body>"""
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


print myTail
















#Format Received
#txtweb-message
#hello
#
#txtweb-id
#fce21192-e59e-440f-b60d-be02f418d1c7
#
#txtweb-verifyid
#94426f5adbc5d9d33638e2cdb36203269a32f799adead9b5e624c6ba0b961ddbdc7fe3e9069c3474aa66a5d0e927991aeaee8cd780b6e0a8cfc07fd984291b5ffaf692ec92553e05cd096c1bc4c40172f48e939313e2574ac57f0f3fa40f452775e385a4d666154187c7c17cea9a3043
#
#txtweb-mobile
#7795ea2d-5dfd-4e06-b244-3c3d24991dfc
#
#txtweb-aggid
#21000
#
#txtweb-protocol
#2100
#
#
#--------
#Check exam results on sms:
#@ANNACOIMB
#@ANNACHENNAI
#
#txtWeb.com
