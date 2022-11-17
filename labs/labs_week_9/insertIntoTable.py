# This prog inserts data into a table in a DB in mysql using a python script. 
# Based on week 9 labs

import mysql.connector

connection = mysql.connector.connect(

    host="localhost",
    user="root",
    password="",
    database="datarepresentation"
)

mycursor = connection.cursor()

sql = "INSERT INTO student ( name, age) values (%s, %s)"
values = ("Mary", 21)

mycursor.execute(sql, values)
connection.commit()
print("1 record inserted, ID:", mycursor.lastrowid)
connection.close()
mycursor.close()