import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database="vickydatabase")
mycursor=mydb.cursor()

mycursor.execute("select * from customers")
myresult=mycursor.fetchone() #fetchone method will return the first row of the result
print(myresult)