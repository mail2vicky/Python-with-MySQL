# you can also set the limit of number of records from the table by using the "limit" statement.

import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database="vickydatabase")
mycursor=mydb.cursor()
# mycursor.execute("select * from customers limit 5")
mycursor.execute("select * from customers limit 5 offset 2")
#here we will start from position 3, and return 5 records
result=mycursor.fetchall()
for i in result:
    print(i)