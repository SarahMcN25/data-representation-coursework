# This prog deletes data from a table in a DB in mysql using a python script. 
# Based on week 9 labs

import mysql.connector

connection = mysql.connector.connect(

    host="localhost",
    user="root",
    password="",
    database="datarepresentation"
)

mycursor = connection.cursor()

sql = "DELETE FROM student WHERE id=%s"
values = (1, )

mycursor.execute(sql, values)
connection.commit()

print("delete done")

connection.close()
mycursor.close()