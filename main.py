from database import *
from tkinter import *
from tkvideo import * # pip install tkvideo
from PIL import ImageTk, Image

from tkinter import messagebox


class Windows(Tk):
    def __init__(self):
        super().__init__()

        self.overrideredirect(True)
        self.geometry("1280x720+150+30")
        my_label = Label(self)
        my_label.pack()
        player = tkvideo("Graphics/SplashScreen/SplashScreen.mp4", my_label, loop=1, size=(1280, 720))
        player.play()
        self.after(5000, self.New_windows)


        # self.master.after(6000, NewWindows)
    def New_windows(self):
        self.withdraw()
        self.win = Toplevel()
        self.win.title("Welcome to GetSetGoal".center(470))
        self.win.geometry("1680x1080+-10+-5")
        self.win.iconbitmap("Graphics/Logo/logo.ico")
        self.win.bg_image = Image.open("background/background.png")
        self.win.bg_image_resized = self.win.bg_image.resize((1530, 880), Image.ANTIALIAS)
        self.win.resized = ImageTk.PhotoImage(self.win.bg_image_resized)
        bg_Img = Label(self.win, image=self.win.resized)
        bg_Img.place(x=0, y=0, relheight=1, relwidth=1)

        # Creating login button and adding icons.
        self.win.btn_login_img = Image.open("Graphics/Logo/login.png")
        self.win.bg_login_resized = self.win.btn_login_img.resize((260, 240), Image.ANTIALIAS)
        self.win.login = ImageTk.PhotoImage(self.win.bg_login_resized)
        btn_login = Button(self.win, image=self.win.login, activebackground="#0066CA", bg="#0066CA", bd=0,command = self.LogWin)
        btn_login.place(x=615, y=350, height=90, width=260)

        # Creating register button and adding icons.
        self.win.btn_register_img = Image.open("Graphics/Logo/register.png")
        self.win.bg_register_resized = self.win.btn_register_img.resize((300, 270), Image.ANTIALIAS)
        self.win.register = ImageTk.PhotoImage(self.win.bg_register_resized)
        btn_register = Button(self.win, image=self.win.register,command = self.RegWin, activebackground="#0066CA", bg="#0066CA", bd=0)
        btn_register.place(x=860, y=355, height=90, width=300)

        # Creating guest button and adding icons
        self.win.btn_guest_img = Image.open("Graphics/Logo/Guest.png")
        self.win.bg_guest_resized = self.win.btn_guest_img.resize((490, 470), Image.ANTIALIAS)
        self.win.guest = ImageTk.PhotoImage(self.win.bg_guest_resized)
        btn_guest = Button(self.win, image=self.win.guest, bg="#0066CA", bd=0, activebackground="#0066CA")
        btn_guest.place(x=640, y=450, height=90, width=490)


    def RegWin(self):
        # global txt_fname
        # global txt_lname
        # global txt_contactno
        # global txt_email
        # global txt_password
        # global txt_gender
        # #
        # txt_fname = StringVar()
        # txt_lname = StringVar()
        # txt_contactno = StringVar()
        # txt_email = StringVar()
        # txt_password = StringVar()
        # txt_gender = StringVar()
        self.win.withdraw()
        self.reg = Toplevel()
        self.reg.title("Registration Form".center(470))
        self.reg.geometry("1680x1080+-10+-5")
        self.reg.iconbitmap("Graphics/Logo/logo.ico")

        self.reg.config(bg="#E9EDF5")
        def insert():
            myConn = Database()
            myCursor = myConn.mydb.cursor()
            try:
                contd = [txt_fname.get()!="", txt_lname.get()!="", txt_email.get()!="", txt_gender.get()!="", txt_contactno.get()!="",
                         txt_password.get()!=""]
                count = str(txt_contactno.get())
                x = len(count)
                if all(contd):
                    if x==10:
                        query = "Insert into tbl_user(first_name,last_name,email,gender,contact_no,password) Values(%s,%s,%s,%s,%s,%s)"
                        value = (txt_fname.get(), txt_lname.get(), txt_email.get(), txt_gender.get(), txt_contactno.get(),
                         txt_password.get())
                        myCursor.execute(query, value)
                        messagebox.showinfo("Registration", "Data Registered Successfully...",parent=self.reg)
                        myConn.mydb.commit()

                        self.reg.withdraw()
                        return self.LogWin()
                    else:
                        messagebox.showerror("Warning!", "Please! Enter 10 digits only.", parent=self.reg)
                else:
                    messagebox.showerror("Warning!","Please! fill all the details........",parent=self.reg)


            except Exception as e:
                print(e)
                myConn.mydb.close()
        # def register():
        #
        #     messagebox.showinfo("Register Successful","You have been registered",parent = self.reg)
        #     self.reg.withdraw()
        #     return self.LogWin()
        # ===Bg Image===
        # reg.bg = ImageTk.PhotoImage(file="logos/4.png")
        # bg_new = Label(reg, image=reg.bg).place(x=50, y=0, relwidth=1, relheight=1)
        self.reg.bg_image = Image.open("Graphics/Logo/4.png")
        self.reg.bg_image_resized = self.reg.bg_image.resize((1530, 840), Image.ANTIALIAS)
        self.reg.resized = ImageTk.PhotoImage(self.reg.bg_image_resized)
        bg_Img = Label(self.reg, image=self.reg.resized)
        bg_Img.place(x=0, y=0, relheight=1, relwidth=1)
        # -------------------Row1
        self.reg.txt_1 = Image.open("Graphics/Logo/txtfield.png")
        self.reg.txt_1_resized = self.reg.txt_1.resize((250, 400), Image.ANTIALIAS)
        self.reg.txt1 = ImageTk.PhotoImage(self.reg.txt_1_resized)
        text_field1 = Label(self.reg,image=self.reg.txt1, bg = "#0066CA",bd=0).place(x=645,y=320,width=270,height=50)
        txt_fname = Entry(self.reg, font=("times new roman", 15),bg = "#E9EDF5",bd=0)
        txt_fname.place(x=657, y=325, width=245, height=40)

        text_field2 = Label(self.reg, image=self.reg.txt1, bg="#0066CA", bd=0).place(x=1005, y=320, width=270, height=50)
        txt_lname = Entry(self.reg, font=("times new roman", 15),bg = "#E9EDF5",bd=0)
        txt_lname.place(x=1017, y=325, width=245, height=40)
        # -------------------Row2


        text_field3 = Label(self.reg, image=self.reg.txt1, bg="#0066CA", bd=0).place(x=1005, y=450, width=270, height=50)
        txt_gender = Entry(self.reg, font=("times new roman", 15),bg="#E9EDF5",bd=0)
        txt_gender.place(x=1017, y=455, width=245, height=40)


        text_field4 = Label(self.reg, image=self.reg.txt1, bg="#0066CA", bd=0).place(x=1005, y=600, width=270,height=50)
        txt_password = Entry(self.reg, font=("times new roman", 15),bg="#E9EDF5",bd=0)
        txt_password.place(x=1017, y=605, width=245, height=40)
        txt_password.config(show="*")
        # -------------------Row3

        text_field5 = Label(self.reg, image=self.reg.txt1, bg="#0066CA", bd=0).place(x=645, y=450, width=270,height=50)
        txt_email = Entry(self.reg, font=("times new roman", 15),bg="#E9EDF5",bd=0)
        txt_email.place(x=657, y=455, width=245, height=40)


        text_field6 = Label(self.reg, image=self.reg.txt1, bg="#0066CA", bd=0).place(x=645, y=600, width=270,height=50)
        txt_contactno = Entry(self.reg, font=("times new roman", 15),bg="#E9EDF5",bd=0)
        txt_contactno.place(x=657, y=605, width=245, height=40)

        # self.reg.btn_login_img = Image.open("logos/login.png")
        # self.reg.bg_login_resized = self.reg.btn_login_img.resize((260, 240), Image.ANTIALIAS)
        # self.reg.login = ImageTk.PhotoImage(self.reg.bg_login_resized)
        # btn_login = Button(self.reg, image=self.reg.login, command=self.LogWin,activebackground="#0066CA", bg="#0066CA", bd=0)
        # btn_login.place(x=655, y=680, height=70, width=240)
        self.reg.btn_register_img = Image.open("Graphics/Logo/register.png")
        self.reg.bg_register_resized = self.reg.btn_register_img.resize((260, 260), Image.ANTIALIAS)
        self.reg.register = ImageTk.PhotoImage(self.reg.bg_register_resized)
        btn_register = Button(self.reg, image=self.reg.register, command=insert, activebackground="#0066CA", bg="#0066CA", bd=0)
        btn_register.place(x=840, y=680, height=80, width=240)

    def LogWin(self):
        self.win.withdraw()
        self.log = Toplevel()
        # Setting the Title of the login Window
        self.log.title("LOGIN".center(470))
        # setting the self.login windows size
        self.log.geometry("1680x1080+-10+-5")
        self.log.iconbitmap("Graphics/Logo/logo.ico")

        def Login():
            myConn = Database()
            user_name = entry_one.get()
            password = entry_two.get()
            try:
                myCur = myConn.mydb.cursor()
                query = "Select email,password from tbl_user"

                myCur.execute(query)
                res = myCur.fetchall()
                for i in res:
                    if str(i[0]==user_name) and str(i[1]==password):
                           messagebox.showinfo("Login Message","Login Successful.")
                           self.log.withdraw()
                    else:
                        messagebox.showerror("Login Error", "Please! Enter Correct Username and Password.")

            except Exception as e:
                print(e)
                myConn.mydb.commit()
                myConn.mydb.close()


        # Adding Background Image

        self.log.bg_image = Image.open("background/3.png")
        self.log.bg_image_resized = self.log.bg_image.resize((1530, 880), Image.ANTIALIAS)
        self.log.resized = ImageTk.PhotoImage(self.log.bg_image_resized)
        bg_Img = Label(self.log, image=self.log.resized)
        bg_Img.place(x=0, y=0, relheight=1, relwidth=1)
        # Creating the User_name entry box.
        # Inserting round shape frame
        self.log.txt_1 = Image.open("Graphics/Logo/txtfield.png")
        self.log.txt_1_resized = self.log.txt_1.resize((300, 400), Image.ANTIALIAS)
        self.log.txt1 = ImageTk.PhotoImage(self.log.txt_1_resized)

        # Adding Round Shape in Entry
        login_label = Label(self.log, image=self.log.txt1, bg="#0066CA", bd=0).place(x=650, y=370,width=320, height=50)
        entry_one = Entry(self.log, border=0, font=("Times New Roman", 15))
        entry_one.config(bg="#E9EDF5")
        entry_one.place(x=662, y=375, width=290, height=40)
        # Creating the password entry box.
        # Adding Round Shape in Entry
        register_label = Label(self.log, image=self.log.txt1, bg="#0066CA", bd=0).place(x=650, y=520,width=320, height=50)
        entry_two = Entry(self.log, border=0, font=("Times New Roman", 15))
        entry_two.place(x=662, y=525, width=290, height=40)
        entry_two.config(show="*", bg="#E9EDF5")
        # Resisizing and implementing the image in the login button.
        self.log.btn_login_img = Image.open("background/4.png")
        self.log.bg_login_resized = self.log.btn_login_img.resize((160, 143), Image.ANTIALIAS)
        self.log.login = ImageTk.PhotoImage(self.log.bg_login_resized)
        btn_login = Button(self.log, image=self.log.login, command = Login,activebackground="#0066CA", bg="#0066CA", bd=0)
        btn_login.place(x=664, y=615, height=60, width=210)
        # Resisizing and implementing the image in the register button.
        self.log.btn_register_img = Image.open("background/5.png")
        self.log.bg_register_resized = self.log.btn_register_img.resize((150, 170), Image.ANTIALIAS)
        self.log.register = ImageTk.PhotoImage(self.log.bg_register_resized)

        btn_register = Button(self.log, image=self.log.register, command=self.RegWin, activebackground="#0066CA", bg="#0066CA",bd=0)
        btn_register.place(x=950, y=595, height=100, width=200)

if __name__ == '__main__':
    root = Windows()
    mainloop()