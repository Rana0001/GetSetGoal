from tkinter import *
from PIL import Image, ImageTk  # pip install pillow


class Registration:
    def __init__(self, root):
        self.root = root
        self.root.title = ("Registration window")
        self.root.geometry("1680x10800+-10+-5")
        self.root.config(bg="#E9EDF5")

        # ===Bg Image===
        self.bg = ImageTk.PhotoImage(file="4.png")
        bg = Label(self.root, image=self.bg).place(x=50, y=0, relwidth=1, relheight=1)

        self.bg_image = Image.open("4.png")
        self.bg_image_resized = self.bg_image.resize((1530, 840), Image.ANTIALIAS)
        self.resized = ImageTk.PhotoImage(self.bg_image_resized)
        bg_Img = Label(self.root, image=self.resized)
        bg_Img.place(x=0, y=0, relheight=1, relwidth=1)
        # -------------------Row1
        txt_fname = Entry(self.root, font=("times new roman", 15)).place(x=655, y=320, width=275, height=50)

        txt_lname = Entry(self.root, font=("times new roman", 15)).place(x=1017, y=320, width=275, height=50)

        # -------------------Row2

        txt_contactno = Entry(self.root, font=("times new roman", 15)).place(x=1017, y=450, width=275, height=50)

        txt_email = Entry(self.root, font=("times new roman", 15)).place(x=1017, y=600, width=275, height=50)

        # -------------------Row3

        txt_password = Entry(self.root, font=("times new roman", 15)).place(x=655, y=450, width=275, height=50)

        txt_gender = Entry(self.root, font=("times new roman", 15)).place(x=655, y=600, width=275, height=50)

        self.btn_login_img = Image.open("1.png")
        self.bg_login_resized = self.btn_login_img.resize((260, 240), Image.ANTIALIAS)
        self.login = ImageTk.PhotoImage(self.bg_login_resized)
        btn_login = Button(self.root, image=self.login, activebackground="#0066CA", bg="#0066CA", bd=0)
        btn_login.place(x=655, y=680, height=70, width=240)

        self.btn_register_img = Image.open("2.png")
        self.bg_register_resized = self.btn_register_img.resize((260, 260), Image.ANTIALIAS)
        self.register = ImageTk.PhotoImage(self.bg_register_resized)
        btn_register = Button(self.root, image=self.register, activebackground="#0066CA", bg="#0066CA", bd=0)
        btn_register.place(x=1017, y=680, height=80, width=240)


root = Tk()
obj = Registration(root)
root.mainloop()

