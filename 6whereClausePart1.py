import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database="vickydatabase")
mycursor=mydb.cursor()
sql = "select * from customers where address like '%pur%' "
mycursor.execute(sql)
result=mycursor.fetchall()
for i in result:
    print(i)
