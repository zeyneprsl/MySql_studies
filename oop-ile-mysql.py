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
        
    def saveStudent(self):
        sql = "INSERT INTO student(StudentNumber, Name, Surname, Birthdate, Gender )  VALUES (%s, %s, %s, %s, %s)"
        value = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender)
        Student.mycursor.execute(sql, value)
        try:
           Student.connection.commit()
           print(f'{Student.mycursor.rowcount} tane kayit eklendi')
        except mysql.connector.errors as err: 
            print("hata",err)
        finally:
            Student.connection.close()

Ayse=Student("107", "zeynep", "persil", datetime.datetime(2001, 6, 15), "k")
Ayse.saveStudent()

