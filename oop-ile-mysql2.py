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
    '''
   Neden Statik Metot Kullandık?
   Sınıfın Örneğine İhtiyaç Yok: bir Student nesnesine ait belirli verilere (örneğin self.studentNumber, self.name gibi) 
   ihtiyaç duymuyor. Bunun yerine, doğrudan bir öğrenci listesi (student listesi) ile çalışıyor. 
   Dolayısıyla, bu fonksiyonu çağırmak için sınıf örneği oluşturmaya gerek yok.
   Sadece öğrenci listesi gönderilerek çalıştırılabiliyor.
    '''
    @staticmethod
    def saveStudent(student):
        sql = "INSERT INTO student(StudentNumber, Name, Surname, Birthdate, Gender )  VALUES (%s, %s, %s, %s, %s)"
        values = student
        Student.mycursor.executemany(sql, values)
        try:
           Student.connection.commit()
           print(f'{Student.mycursor.rowcount} tane kayit eklendi')
        except mysql.connector.errors as err: 
            print("hata",err)
        finally:
            Student.connection.close()

ogrenci = [
        ("201", "Ahmet", "Vilmaz", datetime.datetime(2005, 5, 17), "E"),
        ("202", "Ali", "Can", datetime.datetime(2005, 6, 17),"E"),
        ("203", "Canan", "Tan", datetime.datetime(2005, 7, 7),"K"),
        ("204", "Ayse", "Taner", datetime.datetime(2005, 9, 23), "K"),
        ("205", "Bahadir", "Toksöz", datetime.datetime(2004, 7, 27), "E"),
        ("206", "Ali", "Cenk", datetime.datetime(2003, 8, 25), "E")
        ]
Student.saveStudent(ogrenci)