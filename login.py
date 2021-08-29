import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def Login():
    user_name = entry_one.get()
    password = entry_two.get()

    if (user_name == "" and password == ""):
        messagebox.showinfo("LOGIN","Fill the space.")

    elif(user_name == "" and password == "123"):
        messagebox.showinfo("LOGIN","Fill the space.")

    elif (user_name == "Admin" and password == ""):
        messagebox.showinfo("LOGIN", "Fill the space.")

    elif(user_name=="Admin" and password == "123"):
        messagebox.showinfo("LOGIN", "Login sucessfull")

    else:
        messagebox.showerror("Login ","Icorrect username or passowrd")


root = Tk()

#Setting the Title of the login Window
root.title("L O G I N".center(380))

#setting the login windows size
root.geometry("1280x720")

root.iconbitmap("pictures/logo.ico")

# Adding Background Image

backgroung = ImageTk.PhotoImage(Image.open("pictures/Get_set_goal.png"))

pannel = tkinter.Label(root,image=backgroung)
pannel.place(x=0, y=0)

#Creating the User_name entry box.
entry_one = Entry(root, border = 0, font = ("Times New Roman",25))
entry_one.config(bg="#E9EDF5")
entry_one.place(x= 553, y=320,width=400,height=50)

#Creating the password entry box.
entry_two = Entry(root, border = 0, font = ("Times New Roman",25))
entry_two.place(x= 553, y=440,width=400,height=50)
entry_two.config(show="*",bg="#E9EDF5")

#Resisizing and implementing the image in the login button.
btn_login_img = Image.open("pictures/login.png")
bg_login_resized = btn_login_img.resize((160, 143), Image.ANTIALIAS)
login = ImageTk.PhotoImage(bg_login_resized)
btn_login = Button(root, image=login,activebackground="#0066CA", bg="#0066CA", bd=0,command=Login)
btn_login.place(x=526, y=519, height=60, width=210)

#Resisizing and implementing the image in the register button.
btn_register_img = Image.open("pictures/register.png")
bg_register_resized = btn_register_img.resize((150, 164), Image.ANTIALIAS)
register = ImageTk.PhotoImage(bg_register_resized)
btn_register = Button(root, image=register,activebackground="#0066CA", bg="#0066CA", bd=0)
btn_register.place(x=780, y=498, height=100, width=200)


root.mainloop()

