""" Python needs a MYSql Driver to access the mysql database."""
import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root")
print(mydb)