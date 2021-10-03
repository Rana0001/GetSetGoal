import mysql
from mysql import connector


def connection():
    mydb =  mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="GetSetGoal",
            auth_plugin="mysql_native_password"
            )
    return mydb

def insert(query):
    myConn = connection()
    myCursor = myConn.cursor()

    myCursor.execute(query)

    return 1