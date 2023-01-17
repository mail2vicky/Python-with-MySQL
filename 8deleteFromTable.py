import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database="vickydatabase")
mycursor=mydb.cursor()
sql= "delete from customers where address ='sarai' "
mycursor.execute(sql)
# mydb.commit() if you want to delete permanenttly then uncomment the statement
result=mycursor.fetchall()
print(mycursor.rowcount," Records deleted")
