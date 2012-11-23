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