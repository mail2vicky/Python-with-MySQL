import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database="vickydatabase")
print(mydb)
