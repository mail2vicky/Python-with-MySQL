import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database="vickydatabase")
mycursor=mydb.cursor()
sql = "insert into customers(name,address) values (%s,%s)"
val =("kumod","hajipur")
mycursor.execute(sql,val)
mydb.commit()
print("1 record inserted, ID: ",mycursor.lastrowid)