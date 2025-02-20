import mysql.connector
import datetime
from mysqlconnection import connection

class Student:
    connection = connection
    mycursor = connection.cursor()
    def __init__(self,studentNumber, name, surname, birthdate, gender) :
        self.studentNumber = studentNumber
        self.name = name
        self.birthdate = birthdate
        self.surname = surname
        self.gender = gender
        
    @staticmethod
    def StudentUpdate():
        sql= " update student set studentNumber=studentNumber+1"
        Student.mycursor.execute(sql)
        try:
            connection.commit()
        except mysql.connector.Error as err:
            print("hata",err)
        finally:
             Student.connection.close()
   
    @staticmethod
    def StudentUpdate2(name,studentNumber):
        sql= " update student set name= %s where studentNumber= %s"
        values=(name, studentNumber)
        Student.mycursor.execute(sql,values)
        try:
            connection.commit()
        except mysql.connector.Error as err:
            print("hata",err)
        finally:
             Student.connection.close()
    
    @staticmethod
    def StudentDelete():
        sql= " delete from student where name='Zeynep'"
        Student.mycursor.execute(sql)
        try:
            connection.commit()
        except mysql.connector.Error as err:
            print("hata",err)
        finally:
             Student.connection.close()
        
Student.StudentDelete()