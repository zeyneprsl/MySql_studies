import mysql.connector
from mysqlconnection import connection
mycursor = connection.cursor()
#mycursor.execute("CREATE DATABASE schooldatabase")
mycursor.execute("CREATE TABLE student(id INT AUTO_INCREMENT, studentnumber VARCHAR(255), name VARCHAR(255), surname VARCHAR(255), birthdate DATETIME, gender CHAR(1),PRIMARY KEY (id)) ")
#id INT AUTO_INCREMENT id için böyle atama yap
