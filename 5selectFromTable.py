import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database="vickydatabase")
mycursor=mydb.cursor()

mycursor.execute("select * from customers")
myresult=mycursor.fetchall() #fetches all rows from the last executed statement.
for i in myresult:
    print(i)