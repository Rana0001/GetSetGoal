import mysql.connector


class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="GetSetGoal",
            auth_plugin="mysql_native_password"
            )

