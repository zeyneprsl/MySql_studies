import mysql.connector
import datetime
def insert():
    connection = mysql.connector.connect(host = "localhost", user = "root",password = "zeynep930.",database="schooldatabase")
    ## eger import edersen connection kısmını es gec mycurser ile devam et
    mycursor = connection.cursor()
    sql = "INSERT INTO Student (StudentNumber, Name, Surname, Birthdate, Gender) VALUES (%s, %s, %s, %s, %s)"
    val = [
           ("101", "Ahmet", "Vilmaz", datetime.datetime(2005, 5, 17), "E"),
           ("102", "Ali", "Can", datetime.datetime(2005, 6, 17),"E"),
           ("103", "Canan", "Tan", datetime.datetime(2005, 7, 7),"K"),
           ("104", "Ayse", "Taner", datetime.datetime(2005, 9, 23), "K"),
           ("105", "Bahadir", "Toksöz", datetime.datetime(2004, 7, 27), "E"),
           ("106", "Ali", "Cenk", datetime.datetime(2003, 8, 25), "E")
        ]
    mycursor.executemany(sql, val)

### eğer birden fazla veri eklemek istersen mycursor.execute("")  değil mycursor.executemany("") kullan
    try:
        connection.commit()
        print(f'{mycursor.rowcount} tane kayit eklendi')
    except mysql.connector.errors as err: 
        print("hata",err)
    finally:
        connection.close()

insert()
