import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database="vickydatabase")
mycursor=mydb.cursor()
sql = "insert into customers(name,address) values (%s,%s)"
val = [('vishal','imadpur'),
        ('anoj','imadpur'),
        ('magal','sarai'),
        ('pankaj','hanshi'),
        ('mohan','sarai'),
        ('vinod','koari'),
        ('sukesh','raghunathpur'),
        ('sanjay','bhagwanpur'),
        ('jitendra','mahua'),
        ('vishal','hajiur'),
        ('vikram','imadpur'),
        ]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"rows was inserted")