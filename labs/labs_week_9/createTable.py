# This prog creates a table in a DB in mysql using a python script. 
# Based on week 9 labs

import mysql.connector

connection = mysql.connector.connect(

    host="localhost",
    user="root",
    password="",
    database="datarepresentation"
)

mycursor = connection.cursor()

sql = """
        CREATE TABLE student (
            id int AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age int
        )
    """

mycursor.execute(sql)
connection.close()
mycursor.close()