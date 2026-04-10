from Mysql_Class import Mysql

db = Mysql("Python")
db.connection()

db.create_db("testdb")
db.create_table("testdb", "users", "user_id INT AUTO_INCREMENT PRIMARY KEY, user_name VARCHAR(100) NOT NULL, last_name VARCHAR(100) NOT NULL, user_age INT NOT NULL", )
db.add_user("users", "Ahmet", "Keleş", 24)

db.disconnect()