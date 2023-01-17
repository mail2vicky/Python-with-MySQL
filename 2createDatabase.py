import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root")

"""Here now we will create a database."""
mycursor=mydb.cursor()
# mycursor.execute("create database vickydatabase")

"""Checking if the database exists or not"""

mycursor.execute("show databases")
for i in mycursor:
    print(i)
