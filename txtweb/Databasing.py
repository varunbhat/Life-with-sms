import sqlite3 as lite
class Databasing:
        
    def __init__(self,name,fields,type='a'):
        self.field = fields.keys()
        self.name = name.split('.')[0] 
        fieldType = fields.values()
        self.con = lite.connect(name)
        with self.con:
            cur = self.con.cursor()    
            if type=='w':
                cur.execute("DROP TABLE IF EXISTS "+self.name)
            command= "CREATE TABLE IF NOT EXISTS "+self.name+"(Id INTEGER PRIMARY KEY AUTOINCREMENT"
            for i in range(len(self.field)):
                command = command +','+ self.field[i] +" "+ fieldType[i]
            command = command + ')' 
            cur.execute(command)
#            print command

    def write(self,data):
        listx=[]
#        print data
        with self.con:
            cur = self.con.cursor()
#            print self.name
            cur.execute("SELECT * FROM "+self.name)
            rows = cur.fetchall()
#            print "i'm here",rows
#            for row in rows:
#                for i in range(len(self.field)):
#                    if data[self.field[i]] in row:
##                        print data[self.field[i]] , 'repeated'
#                        return 2
#                        break
            command = "INSERT INTO "+self.name+"("+self.field[0]
            listx.append(data[self.field[0]])
            for i in reversed(range(1,len(self.field))):
                command = command+','+self.field[i]
                listx.append(data[self.field[i]])
            command = command + ') VALUES (?'
            for i in range(1,len(self.field)):
                command = command + ',?'
            command = command + ')'
            cur.execute(command,listx)
            return 0

    def read(self):
        with self.con:
            cur = self.con.cursor()
            cur.execute("SELECT * FROM "+self.name)
            rows = cur.fetchall()
            for row in rows:
                print row  
                print "<br>"
            
    def update(self,field,update,otherField,constField):
        with self.con:
            cur = self.con.cursor()
            command = 'UPDATE '+self.name+' SET '+field+' = '+ update+' WHERE '+otherField +' = '+constField
            print command
            cur.execute(command)



#    def deleteDB(self):
#        con = lite.connect('Donor.db')
#        with con:    
#            cur = con.cursor()   
#            cur.execute("DROP TABLE IF EXISTS Donors")