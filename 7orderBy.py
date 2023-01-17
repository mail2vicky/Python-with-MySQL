# order by statement: sorting the result in asce and desc order

import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database="vickydatabase")
mycursor=mydb.cursor()
sql = "select * from customers order by name "
mycursor.execute(sql)
result=mycursor.fetchall()
for i in result:
    print(i)
