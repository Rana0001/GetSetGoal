from tkinter import *
import pyttsx3
import wikipedia
from PIL import ImageTk, Image
from tkvideo import *
from tkinter import messagebox


def user_panel():
    upanel = Toplevel()
    upanel.title("Welcome to GetSetGoal".center(470))
    upanel.geometry("1680x1080+-10+-5")
    upanel.iconbitmap("Graphics/Logo/logo.ico")
    bg_image = Image.open("background/UserBack.png")
    upanel.bg_image_resized = bg_image.resize((1530, 880), Image.ANTIALIAS)
    upanel.resized = ImageTk.PhotoImage(upanel.bg_image_resized)
    bg_Img = Label(upanel, image=upanel.resized)
    bg_Img.place(x=0, y=0, relheight=1, relwidth=1)

    def dash():
        return 0

    def logout():
        result =  messagebox.askquestion("LOG OUT".center(90),"Are you sure you want to log out?")
        if result == 'yes':
            return upanel.destroy()
        else:
            return 0


    def mvp():

        def describe():
            engine = pyttsx3.init()
            player = wikipedia.summary("Karim Benzema",2)
            voices = engine.getProperty("voices")
            engine.setProperty('voice',voices[1].id)
            engine.say(player)
            engine.runAndWait()
        bg_image = Image.open("background/UserBack.png")
        upanel.bg_image_resized = bg_image.resize((1530, 880), Image.ANTIALIAS)
        upanel.resized = ImageTk.PhotoImage(upanel.bg_image_resized)
        bg_Img = Label(upanel, image=upanel.resized)
        bg_Img.place(x=350, y=0, relheight=1, relwidth=1)

        title_img = Image.open("mvp/title.png")
        upanel.title_resized = title_img.resize((800, 70), Image.ADAPTIVE)
        upanel.mvp_title_image = ImageTk.PhotoImage(upanel.title_resized)
        mvp_title = Label(upanel, image=upanel.mvp_title_image, bg="#0066CA")
        mvp_title.place(x=380, y=50, height=70, width=800)

        man_img = Image.open("mvp/player.png")
        upanel.man_resized = man_img.resize((350, 550), Image.ADAPTIVE)
        upanel.mvp_banner_image = ImageTk.PhotoImage(upanel.man_resized)
        mvp_lbl = Label(upanel, image=upanel.mvp_banner_image, bg="#0066CA")
        mvp_lbl.place(x=700, y=290, height=550, width=350)

        name_img = Image.open("mvp/name.png")
        upanel.name_resized = name_img.resize((350, 190), Image.ADAPTIVE)
        upanel.mvp_name_image = ImageTk.PhotoImage(upanel.name_resized)
        mvp_name = Label(upanel, image=upanel.mvp_name_image, bg="#0066CA")
        mvp_name.place(x=1150, y=280, height=200, width=350)

        club_img = Image.open("mvp/club.png")
        upanel.club_resized = club_img.resize((350, 190), Image.ADAPTIVE)
        upanel.mvp_club_image = ImageTk.PhotoImage(upanel.club_resized)
        mvp_club = Label(upanel, image=upanel.mvp_club_image, bg="#0066CA")
        mvp_club.place(x=1150, y=480, height=200, width=350)

        # info_icon = ImageTk.PhotoImage(Image.open("mvp/info.png"))
        btn_info = Button(upanel,text="i",font=("Cambria",25,"italic"),command=describe,bd=0,relief = RIDGE,bg="#E9EDF5",fg="#0066CA",activebackground="#E9EDF5",activeforeground="#0066CA")
        btn_info.place(x=1300,y=230,height=40,width=40)


    frame = Frame(upanel, bd=3, highlightthickness=5, highlightcolor="#1a2b63", highlightbackground="#1a2b63",
                  bg="#E9EDF5")
    frame.place(x=5, y=0, height=835, width=350)
    label = Label(text=f"WELCOME", font=("cambria", 16, "bold"), fg="#0066CA", bg="#E9EDF5")
    label.place(x=120, y=200)

    user_image = ImageTk.PhotoImage(Image.open("userpanel_graphics/user_icon.png"))
    user_lbl = Label(upanel, image=user_image, bg="#E9EDF5")
    user_lbl.place(x=110, y=50)

    my_label = Label(upanel)
    my_label.place(x=390, y=35, height=370, width=650)
    player = tkvideo("Graphics/banner/intro.mp4", my_label, loop=1, size=(640, 360))
    player.play()

    match_img = Image.open("userpanel_graphics/match.png")
    match_resized = match_img.resize((330, 220), Image.ANTIALIAS)
    match_image = ImageTk.PhotoImage(match_resized)
    match_lbl = Label(upanel, image=match_image, bg="#0066CA")
    match_lbl.place(x=385, y=440, height=220, width=330)

    bottom_img = Image.open("userpanel_graphics/bottom_banner.png")
    bottom_resized = bottom_img.resize((940, 95), Image.ANTIALIAS)
    bbanner_img = ImageTk.PhotoImage(bottom_resized)
    bottom_lbl = Label(upanel, image=bbanner_img, bg="#0066CA")
    bottom_lbl.place(x=460, y=740, height=75, width=950)

    # Dashboard Button

    btn_dash = Button(upanel, text="DASHBOARD          ",command=dash, font=("Cambria",16,"bold"), fg="#0066CA",bg="#E9EDF5",
                      activebackground="#E9EDF5",activeforeground="#0066CA",bd=0)
    btn_dash.place(x=70, y=250, width=230, height=50)
    dash_img = Image.open("menu_icons/1.png")
    dash_resized = dash_img.resize((50, 50), Image.ANTIALIAS)
    dash_image = ImageTk.PhotoImage(dash_resized)
    dash_lbl = Label(upanel,image=dash_image, bg="#E9EDF5")
    dash_lbl.place(x=30,y=250,height = 50, width=50)

    # League Button

    btn_league = Button(upanel, text=" LEAGUE TABLE", font=("Cambria",16,"bold"),activebackground="#E9EDF5",activeforeground="#0066CA", fg="#0066CA",bg="#E9EDF5", bd=0)
    btn_league.place(x=78, y=310, width=180, height=50)
    league_img = Image.open("menu_icons/2.png")
    league_resized = league_img.resize((50, 50), Image.ANTIALIAS)
    league_image = ImageTk.PhotoImage(league_resized)
    league_lbl = Label(upanel, image=league_image,  bg="#E9EDF5")
    league_lbl.place(x=27, y=310, height=50, width=50)

    # Player of the month button
    mvp_img = Image.open("menu_icons/3.png")
    mvp_resized = mvp_img.resize((50, 50), Image.ANTIALIAS)
    mvp_image = ImageTk.PhotoImage(mvp_resized)
    btn_mvp = Button(upanel,text=" PLAYER OF THE MONTH", activebackground="#E9EDF5",activeforeground="#0066CA",font=("Cambria",16,"bold"), fg="#0066CA", command=mvp, bg="#E9EDF5", bd=0)
    btn_mvp.place(x=85, y=370, width=250, height=50)
    mvp_lbl = Label(upanel, image=mvp_image, bg="#E9EDF5")
    mvp_lbl.place(x=24, y=370, height=50, width=50)

    # # Top Goal Scorer button
    top_img = Image.open("menu_icons/4.png")
    top_resized = top_img.resize((50, 50), Image.ANTIALIAS)
    top_image = ImageTk.PhotoImage(top_resized)
    top_btn = Button(upanel, text="TOP SCORERS               ", font=("Cambria",16,"bold"), activebackground="#E9EDF5",activeforeground="#0066CA",fg="#0066CA", bg="#E9EDF5", bd=0)
    top_btn.place(x=85, y=430, width=230, height=50)
    top_lbl = Label(upanel, image=top_image, bg="#E9EDF5")
    top_lbl.place(x=24, y=430, height=50, width=50)
    #
    # # Update Profiles Button
    update_img = Image.open("menu_icons/5.png")
    update_resized = update_img.resize((50, 50), Image.ANTIALIAS)
    update_image = ImageTk.PhotoImage(update_resized)
    update_btn = Button(upanel, text="UPDATE PROFILE            ", font=("Cambria",16,"bold"), activebackground="#E9EDF5",activeforeground="#0066CA",fg="#0066CA", bg="#E9EDF5", bd=0)
    update_btn.place(x=87, y=490, width=250, height=50)
    update_lbl = Label(upanel, image=update_image, bg="#E9EDF5")
    update_lbl.place(x=24, y=490, height=50, width=50)
    #
    # # Play Quiz Button
    quiz_img = Image.open("menu_icons/6.png")
    quiz_resized = quiz_img.resize((50, 50), Image.ANTIALIAS)
    quiz_image = ImageTk.PhotoImage(quiz_resized)
    quiz_btn = Button(upanel, text=" PLAY QUIZ                      ", activebackground="#E9EDF5",activeforeground="#0066CA",font=("Cambria",16,"bold"), fg="#0066CA", bg="#E9EDF5", bd=0)
    quiz_btn.place(x=78, y=550, width=250, height=50)
    quiz_lbl = Label(upanel, image=quiz_image, bg="#E9EDF5")
    quiz_lbl.place(x=24, y=550, height=50, width=50)

    # Log out button
    log_img = Image.open("menu_icons/7.png")
    log_resized = log_img.resize((50, 50), Image.ANTIALIAS)
    log_image = ImageTk.PhotoImage(log_resized)
    log_btn = Button(upanel, text="  LOG OUT                          ", activebackground="#E9EDF5",activeforeground="#0066CA",font=("Cambria",16,"bold"), fg="#0066CA", command=logout, bg="#E9EDF5", bd=0)
    log_btn.place(x=78, y=750, width=250, height=50)
    log_lbl = Label(upanel, image=log_image, bg="#E9EDF5")
    log_lbl.place(x=24, y=750, height=50, width=50)

    upanel.mainloop()


