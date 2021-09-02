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
    frame.place(x=5,y=0,height= 835,width = 350)
    label = Label(text=f"WELCOME",font= ("Futura",15,"bold"),fg = "#0066CA")
    label.place(x= 120, y= 200)


    my_label = Label(upanel)
    my_label.place(x=390,y=35,height=370,width=650)
    player = tkvideo("Graphics/banner/intro.mp4", my_label, loop=1, size=(640, 360))
    player.play()

    match_img = Image.open("userpanel_graphics/match.png")
    match_resized = match_img.resize((330, 220), Image.ANTIALIAS)
    match_image = ImageTk.PhotoImage(match_resized)
    match_lbl = Label(upanel,image= match_image,bg= "#0066CA")
    match_lbl.place(x=385,y=440,height=220,width=330)



    bottom_img = Image.open("userpanel_graphics/bottom_banner.png")
    bottom_resized = bottom_img.resize((940, 95), Image.ANTIALIAS)
    bbanner_img = ImageTk.PhotoImage(bottom_resized)
    bottom_lbl = Label(upanel,image= bbanner_img,bg= "#0066CA")
    bottom_lbl.place(x=460,y=740,height=75,width=950)

    upanel.mainloop()



user_panel()
