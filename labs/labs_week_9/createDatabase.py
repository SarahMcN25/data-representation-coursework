# This prog creates a database in mysql using a python script. 
# Based on week 9 labs

import mysql.connector

connection = mysql.connector.connect(

    host="localhost",
    user="root",
    password=""
)

mycursor = connection.cursor()

mycursor.execute(

    "CREATE DATABASE datarepresentation"
)

connection.close()
mycursor.close()