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


    frame = Frame(upanel,bd=3,highlightthickness= 5,highlightcolor="#1a2b63",highlightbackground="#1a2b63",bg="#E9EDF5")
    frame.place(x=5,y=0,height= 835,width = 350)
    label = Label(text=f"WELCOME",font= ("Futura",15,"bold"),fg = "#0066CA",bg="#E9EDF5")
    label.place(x= 120, y= 200)

    user_image = ImageTk.PhotoImage(Image.open("userpanel_graphics/user_icon.png"))
    user_lbl = Label(upanel,image=user_image,bg="#E9EDF5")
    user_lbl.place(x=110,y= 50)

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

# Dashboard Button
    dash_img = Image.open("menu_icons/dashboard.png")
    dash_resized = dash_img.resize((345, 68), Image.ANTIALIAS)
    dash_image = ImageTk.PhotoImage(dash_resized)
    btn_dash = Button(upanel,image = dash_image,bg="#E9EDF5",bd=0)
    btn_dash.place(x= 12,y=250,width= 335,height=60)

# League Button
    league_img = Image.open("menu_icons/league.png")
    league_resized = league_img.resize((340, 80), Image.ANTIALIAS)
    league_image = ImageTk.PhotoImage(league_resized)
    btn_league = Button(upanel, image=league_image, bg="#E9EDF5", bd=0)
    btn_league.place(x=37, y=310, width=310, height=60)

# Player of the month button
    mvp_img = Image.open("menu_icons/player.png")
    mvp_resized = mvp_img.resize((350, 75), Image.ANTIALIAS)
    mvp_image = ImageTk.PhotoImage(mvp_resized)
    btn_mvp = Button(upanel, image=mvp_image, bg="#E9EDF5", bd=0)
    btn_mvp.place(x=37, y=370, width=305, height=60)

    # bottom_lbl = Label(upanel,image= dash_image,bg= "#E9EDF5")
    # bottom_lbl.place(x=30,y=250,height=40,width=320)


    upanel.mainloop()



user_panel()
