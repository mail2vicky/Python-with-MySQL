# you can update the existing records in a table by using "update" statement.

import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database="vickydatabase")
mycursor=mydb.cursor()
sql = "update customers set name = 'vikash' where name ='vicky' "
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount," record updated.")
