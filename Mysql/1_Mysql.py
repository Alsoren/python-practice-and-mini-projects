import mysql.connector

connection = mysql.connector.connect(host="localhost",user="root",password="",database="newdb") # Bağlantı oluşturulur
mycursor = connection.cursor() # Cursor oluşturulur

mycursor.execute("CREATE DATABASE IF NOT EXISTS newdb") # Data base oluşturulur
mycursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), last_name VARCHAR(255), user_age INT) ENGINE=InnoDB") # Kullanıcılar tablosu oluşturulur
mycursor.execute("ALTER TABLE users DROP COLUMN email1 ") # Email sütunu eklenir

mycursor.close()
connection.close() 