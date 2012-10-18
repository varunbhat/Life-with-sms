from Databasing import Databasing
mydb = Databasing('forceNumber.db',{'Name':'TEXT','Phone':'TEXT','Level':'INT'},'w')
f = open('contacts.csv','r')
data=f.read()
data = data.replace('\t','')
data= data.split('\n')
for i in range(len(data)):
    data[i] = data[i].split(':')
    
for i in data:
    try:
        i[1]
    except:
        break
        
    i[1] = i[1].replace(' ','')
    i[0] = i[0].replace('.',' ')
    cont = {'Name':i[0],'Phone':i[1],'Level':''}
    mydb.write(cont)
mydb.read()

