import cgi

class donorValidate: 
    def __init__(self):           
        form = cgi.FieldStorage()
        self.hash = form.getvalue('txtweb-mobile')
        self.userMsg = form.getvalue('txtweb-message')
#        self.userMsg = 'dijin dan 7732384179'
        verifyId = form.getvalue('txtweb-verifyid')
        txtWebId = form.getvalue('txtweb-id')
        
        def isAlpha(dat):
            try:
                x = int(dat)
                return False
            except:
                return True
        
        if self.userMsg=='':
            print "i'll give u the details how to message later guys"
            return 1
        else:
            mydata = self.userMsg.upper()
            mydata = mydata.split(' ')
            for temp in mydata:
                if not isAlpha(temp):
                    if len(temp)==10:
                        self.numb = temp
                        temp = mydata.index(temp)
                        mydata.pop(temp)
                        break
            self.name = ' '.join(mydata[0:temp])
    def get(self):
        return {'Name':self.name ,'Hash':self.hash,'Phone':self.numb}