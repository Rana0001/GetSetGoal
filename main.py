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
        player = tkvideo("SplashScreen/SplashScreen.mp4", my_label, loop=1, size=(1280, 720))
        player.play()
        self.after(5000, self.New_windows)


        # self.master.after(6000, NewWindows)
    def New_windows(self):
        self.withdraw()
        self.win = Toplevel()
        self.win.title("Welcome to GetSetGoal".center(470))
        self.win.geometry("1680x1080+-10+-5")
        self.win.iconbitmap("logos/logo.ico")
        self.win.bg_image = Image.open("background/background.png")
        self.win.bg_image_resized = self.win.bg_image.resize((1530, 880), Image.ANTIALIAS)
        self.win.resized = ImageTk.PhotoImage(self.win.bg_image_resized)
        bg_Img = Label(self.win, image=self.win.resized)
        bg_Img.place(x=0, y=0, relheight=1, relwidth=1)

        # Creating login button and adding icons.
        self.win.btn_login_img = Image.open("logos/login.png")
        self.win.bg_login_resized = self.win.btn_login_img.resize((260, 240), Image.ANTIALIAS)
        self.win.login = ImageTk.PhotoImage(self.win.bg_login_resized)
        btn_login = Button(self.win, image=self.win.login, activebackground="#0066CA", bg="#0066CA", bd=0,command = self.LogWin)
        btn_login.place(x=615, y=350, height=90, width=260)

        # Creating register button and adding icons.
        self.win.btn_register_img = Image.open("logos/register.png")
        self.win.bg_register_resized = self.win.btn_register_img.resize((300, 270), Image.ANTIALIAS)
        self.win.register = ImageTk.PhotoImage(self.win.bg_register_resized)
        btn_register = Button(self.win, image=self.win.register,command = self.RegWin, activebackground="#0066CA", bg="#0066CA", bd=0)
        btn_register.place(x=860, y=355, height=90, width=300)

        # Creating guest button and adding icons
        self.win.btn_guest_img = Image.open("logos/Guest.png")
        self.win.bg_guest_resized = self.win.btn_guest_img.resize((490, 470), Image.ANTIALIAS)
        self.win.guest = ImageTk.PhotoImage(self.win.bg_guest_resized)
        btn_guest = Button(self.win, image=self.win.guest, bg="#0066CA", bd=0, activebackground="#0066CA")
        btn_guest.place(x=640, y=450, height=90, width=490)



if __name__ == '__main__':
    root = Windows()
    mainloop()