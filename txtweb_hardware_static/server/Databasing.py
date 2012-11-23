import sqlite3 as lite
class Databasing:
    def __init__(self, name, fields, type='a'):
        self.field = fields.keys()
        self.name = name.split('.')[0] 
        fieldType = fields.values()
        self.con = lite.connect(name)
        with self.con:
            cur = self.con.cursor()    
            if type == 'w':
                cur.execute("DROP TABLE IF EXISTS " + self.name)
            command = "CREATE TABLE IF NOT EXISTS " + self.name + "(Id INTEGER PRIMARY KEY AUTOINCREMENT"
            for i in range(len(self.field)):
                command = command + ',' + self.field[i] + " " + fieldType[i]
            command = command + ')' 
            cur.execute(command)

    def write(self, data):
        listx = []
        with self.con:
            cur = self.con.cursor()
            cur.execute("SELECT * FROM " + self.name)
            rows = cur.fetchall()
            command = "INSERT INTO " + self.name + "(" + self.field[0]
            listx.append(data[self.field[0]])
            for i in reversed(range(1, len(self.field))):
                command = command + ',' + self.field[i]
                listx.append(data[self.field[i]])
            command = command + ') VALUES (?'
            for i in range(1, len(self.field)):
                command = command + ',?'
            command = command + ')'
            cur.execute(command, listx)
            return 0

    def read(self, rowNum=-1,rowx=()):
        with self.con:
            cur = self.con.cursor()
            if rowx == ():
                cur.execute("SELECT * FROM " + self.name)
            else:
                rowxc = ','.join(rowx[0:len(rowx)])
                cur.execute("SELECT "+rowxc+" FROM " + self.name)
                
            rows = cur.fetchall()
            if rowNum == -1:
                return rows
#                for row in rows:
#                    print row  
#                    print "<br>"
            elif rowNum == 0:
                return rows[len(rows)-1]
#                print rows[len(rows)-1]
            else:
                return rows[len(rows)-1]
#                print rows[len(rows)-1]

    def update(self, field, update, otherField, constField):
        with self.con:
            cur = self.con.cursor()
            command = 'UPDATE ' + self.name + ' SET ' + field + ' = ' + update + ' WHERE ' + otherField + ' = ' + constField
#            print command
            cur.execute(command)

    def deleteDB(self):
        con = lite.connect(self.name+'.db')
        with con:    
            cur = con.cursor()   
            cur.execute("DROP TABLE IF EXISTS Donors")
