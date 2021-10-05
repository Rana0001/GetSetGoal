from database import *


def login(email, password):
    myConn = Database()
    myCur = myConn.mydb.cursor()
    query = f"Select email,password from tbl_user where email='{email}' and password='{password}'"
    myCur.execute(query)
    result = myCur.fetchall()

    if result:
        return "Pass"
    else:
        return "Fail"

def register(first_name,last_name,email,password,gender,contact_no):
    myConn = Database()
    myCur = myConn.mydb.cursor()
    query=f"INSERT INTO tbl_user(first_name,last_name,email,password,gender,contact_no) VALUES('{first_name}','{last_name}','{email}','{password}','{contact_no}','{gender}')"
    myCur.execute(query)

def delete(email):
    myConn = Database()
    myCur = myConn.mydb.cursor()
    query = f"Delete from tbl_user where email='{email}'"
    myCur.execute(query)

def update(first_name,last_name,email):
    myConn = Database()
    myCur = myConn.mydb.cursor()
    query = f"Update tbl_user set first_name = '{first_name}',last_name='{last_name}' where email ='{email}'"
    myCur.execute(query)