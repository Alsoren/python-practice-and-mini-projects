import mysql.connector

class Mysql:
    def __init__(self, database):
        self.__host = "localhost"
        self.__user = "root"
        self.__password = "root"
        self.__database = database
        self.__connection = None
        self.__cursor = None

    def connection(self):
        self.__connection = mysql.connector.connect(
            host=self.__host,
            user=self.__user,
            password=self.__password,
            database=self.__database)
        
        if self.__connection.is_connected():
            self.__cursor = self.__connection.cursor()
            print("Connected succesfuly")
        else:
            print("Connection Failed!")
    
    def create_db(self, db_name, charset="utf8mb4", collation="utf8mb4_0900_ai_ci"):
        sql = f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET {charset} COLLATE {collation}"
        self.__cursor.execute(sql)
        print(f"{db_name} database created succesfully.")

    def create_table(self, db_name, table_name, columns):
        self.__cursor.execute(f"USE {db_name}")
        self.__cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns}) ENGINE=InnoDB")
        print(f"{table_name} table created succesfully.")

    def add_user(self,table_name, name, last_name, age):
        sql = f"INSERT INTO {table_name}(user_name, last_name, user_age) values(%s,%s,%s)"
        values = (name, last_name, age)
        self.__cursor.execute(sql, values)
        self.__connection.commit()
        print(f"ID: {self.__cursor.lastrowid}, Name: {name} {last_name} has been added")
        
    def add_users(self,table_name, users):
        sql = f"INSERT INTO {table_name}(user_name, last_name, user_age) values(%s,%s,%s)"
        self.__cursor.executemany(sql, users) # Bir çok kayıtı liste olarak ekleme
        self.__connection.commit()
        print(f"ID: {self.__cursor.rowcount}, record inserted!")

    def delete_user(self, table_name, user_id):
        sql = f"DELETE FROM {table_name} WHERE user_id = %s"
        self.__cursor.execute(sql, (user_id,))
        self.__connection.commit()
        print(f"ID: {user_id} has been deleted")


    def disconnect(self):
        if self.__cursor:
            self.__cursor.close()
        if self.__connection:
            self.__connection.close()