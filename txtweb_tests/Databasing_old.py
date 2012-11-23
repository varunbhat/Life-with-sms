class Databaseing:
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