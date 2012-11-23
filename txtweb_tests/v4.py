#!/usr/bin/env python
from txtweb import txtweb
from Databasing import Databasing 
from donorValidate import donorValidate 


class basic(txtweb):
    def insert(self):
        self.myevalx = donorValidate()
        myvals = {'Name':"TEXT",'Phone':"TEXT",'Hash':'TEXT'}
        myDon = Databasing('revolution.db',myvals)
        a = myDon.write(self.myevalx.get())
#        a=0
        if a==0:
            print 'Thank u thank u, keep up the hard work'
        elif a==2:
            print 'Do u like to waste msgs???!! Keep them for ur gf/bf'
        print myDon.read()


x = basic('07093fda-d254-4e77-a2bc-c3dc74a63baa')
x.insert()
x.close()