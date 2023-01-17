import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database="vickydatabase")
mycursor=mydb.cursor()
# mycursor.execute("create table customers (name varchar(255), address varchar(255))")
mycursor.execute("show tables")
for i in mycursor:
    print(i)