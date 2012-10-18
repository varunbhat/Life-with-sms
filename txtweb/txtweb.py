#import urllib2
import cgi
#import sqlite3 as lite
import sys
#import push,doner
from urllib import urlopen

class txtweb:
    def __init__(self, appid):
        self.appid = appid
        self.form = cgi.FieldStorage()
        self.hash = self.form.getvalue('txtweb-mobile')
        self.userMsg = self.form.getvalue('txtweb-message')
        self.verifyId = self.form.getvalue('txtweb-verifyid')
        self.txtWebId = self.form.getvalue('txtweb-id')
        self.pubId = "dd29f986-9a8b-4252-8bc8-f319644932b2"
        print "Content-type: text/html\r\n\r\n"
        self.printHead()
    
    def printHead(self):
        myHeader = """<html>
    <head>
        <title> Hello! </title>
        <meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
        <meta name='txtweb-appkey' content='""" + self.appid + """' />
    </head>
        <body>"""
        print myHeader
    
    def close(self):
        myTail = """</body>
    <html>"""
        print myTail