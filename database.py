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
        if self.mydb != 0:
            print("Connection Successfull")
        # myCur = self.mydb.cursor()
        # # myCur1 = self.mydb.cursor()
        # query = "Select email,password from tbl_user"
        # # # query1 = "Delete from tbl_user"
        # myCur.execute(query)
        # # # myCur1.execute(query1)
        # res = myCur.fetchall()
        # for i in res:
        #     print(i[1])



Database()

# def insert():
#

# myConn = Database()
#     myCursor = myConn.mydb.cursor()
#     try:
#         query = "Insert into tbl_user(first_name,last_name,email,gender,contact_no,password) Values(%s,%s,%s,%s,%s,%s)"
#         value = (txt_fname.get(), txt_lname.get(), txt_email.get(), txt_gender.get(), txt_contactno.get(), txt_password.get())
#         myCursor.execute(query,value)
#         messagebox.showinfo("Registration", "Data Registered Successfully...")
#         myConn.mydb.commit()
#     except Exception as e:
#         print(e)
#         myConn.mydb.close()
# def print():
#     print(txt_fname.get())
# #
    # def insert(self):
    #     self.mycursor = self.mydb.cursor()
    #     try:
    #     #     sql = "INSERT INTO tbl_user VALUES(%s,%s,%s,%s,%s,%s)"
    #     #     val = (Windows.RegWin.txt_fname.get(), lname, cont, e_mail, pass_word, gen)
    #     #     self.mycursor.execute(sql, val)
    #     #     self.mydb.commit()
    #     #     messagebox.showinfo("Registeration", "Data regestrated Sucessfully.")
    #     # except Exception as e:
    #     #     print(e)
    #     #     self.mydb.close()
