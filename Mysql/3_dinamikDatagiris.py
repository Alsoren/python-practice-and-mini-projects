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
        
    def disconnect(self):
        if self.__cursor:
            self.__cursor.close()
        if self.__connection:
            self.__connection.close()

db = Mysql("Python")
db.connection()

while True:
    print("\n1- Add User")
    print("2- Exit")
    choice = int(input("Enter your choice (1/2): "))
    if choice == 1:
        first_name = input("Enter first name: ").strip()
        last_name = input("Enter last name: ").strip()
        age = int(input("Enter age: ").strip())
        user_data = {"user_name":first_name, "user_lastname": last_name, "user_age": age}
        db.insert_record("", user_data)

    elif choice == 2:
        break
    else:
        print("Invalid choice. Please try again.")
        continue
db.disconnect()
