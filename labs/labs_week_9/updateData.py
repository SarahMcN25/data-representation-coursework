# This prog updates data in a table in a DB in mysql using a python script. 
# Based on week 9 labs

import mysql.connector

connection = mysql.connector.connect(

    host="localhost",
    user="root",
    password="",
    database="datarepresentation"
)

mycursor = connection.cursor()

sql = "UPDATE student set name=%s, age=%s where id=%s"
values = ("Joe", 33, 1)

mycursor.execute(sql, values)
connection.commit()

print("update done")

connection.close()
mycursor.close()