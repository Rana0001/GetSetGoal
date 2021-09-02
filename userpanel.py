from tkinter import *
from PIL import ImageTk, Image
from tkvideo import *

def user_panel():
    upanel = Tk()
    upanel.title("Welcome to GetSetGoal".center(470))
    upanel.geometry("1680x1080+-10+-5")
    upanel.iconbitmap("Graphics/Logo/logo.ico")
    bg_image = Image.open("background/UserBack.png")
    upanel.bg_image_resized = bg_image.resize((1530, 880), Image.ANTIALIAS)
    upanel.resized = ImageTk.PhotoImage(upanel.bg_image_resized)
    bg_Img = Label(upanel, image=upanel.resized)
    bg_Img.place(x=0, y=0, relheight=1, relwidth=1)


    frame = Frame(upanel,bd=3,highlightthickness= 5,highlightcolor="#1a2b63",highlightbackground="#1a2b63")
    frame.place(x=5,y=0,height= 790,width = 350)
    label = Label(text=f"Welcome",font= ("Cambria",15,"bold"),fg = "Black")
    label.place(x= 150, y= 200)

    # player_img = Image.open("userpanel_graphics/banner.png")
    # player_resized = player_img.resize((1280, 400), Image.ANTIALIAS)
    # player_img = ImageTk.PhotoImage(player_resized)
    my_label = Label(upanel)
    my_label.place(x=400,y=5,height=300,width=1000)
    player = tkvideo("Graphics/SplashScreen/SplashScreen.mp4", my_label, loop=1, size=(950, 280))
    player.play()
    # upanel.after(5000, self.New_windows)


    upanel.mainloop()

user_panel()
