# This contains a class for StudentDAO which can be used in another file. 
# Based on week 9 labs

import mysql.connector

class StudentDAO:
    host =""
    user = ""
    password =""
    database =""
    connection = ""
    cursor =""


    def __init__(self): 
        #these should be read from a config file
        self.host="localhost"
        self.user="root"
        self.password=""
        self.database="datarepresentation"

      
    def getCursor(self): 
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor


    def closeAll(self):
        self.connection.close()
        self.cursor.close()
    

    def create(self, values):
        cursor = self.getCursor()
        sql="INSERT INTO student (name, age) VALUES (%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid


    def getAll(self):
        cursor = self.getCursor()
        sql="SELECT * FROM student"
        cursor.execute(sql)
        result = cursor.fetchall()
        self.closeAll()
        return result


    def findByID(self, id):
        cursor = self.getCursor()
        sql="SELECT * FROM student WHERE id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return result


    def update(self, values):
        cursor = self.getCursor()
        sql="UPDATE student SET name= %s, age=%s  WHERE id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()


    def delete(self, id):
        cursor = self.getCursor()
        sql="DELETE FROM student WHERE id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll
        print("delete done")


studentDAO = StudentDAO()