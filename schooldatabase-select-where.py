"""
fetchall() metodu, sorgudan dönen tüm satırları bir seferde alır ve bir liste olarak döner.
Satırların Yapısı: Dönen her satır genellikle bir tuple formatındadır. Eğer sütun sayısı 5 ise, her tuple 5 eleman içerir.
cursor.fetchone(): Sorgudan sadece bir satır döner. Tek bir sonuç almak istediğinizde kullanılır.
cursor.fetchmany(size): Sorgudan belirtilen sayıda (örneğin 10) satırı alır.
"""
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
    def studendInfo():
        #sql = "SELECT * FROM student"
        sql= "select studentnumber , name, surname from student"
        #sql= "select * from  student where YEAR(birthdate)=2003"
        #sql= "select * from  student where YEAR(birthdate)=2005 and name='Ali'"
        #sql="select studentnumber , name, surname from student where gender='K'"
        #sql= "select * from  student where name like '%an%'"
        #sql= "select COUNT(*) from  student where  gender='K'"
        #sql= "select COUNT(*) from  student where  gender='K' ORDER BY name"
        Student.mycursor.execute(sql)
        try:
            connection.commit()
            result = Student.mycursor.fetchall()
            for row in result:
                    #print(row)
                    print(f'{row[0]} {row[1]} {row[2]}')
        except mysql.connector.Error as err:
             print("hata",err)
        finally:
             Student.connection.close()

Student.studendInfo()