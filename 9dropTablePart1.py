# you can delete an existing table by using the "drop table" statement.
import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database="vickydatabase")
mycursor=mydb.cursor()
sql ="drop table if exists customers"
mycursor.execute(sql)
