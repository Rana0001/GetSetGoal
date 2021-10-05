import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from PIL import ImageTk, Image
from tkvideo import *

from database import *



user_name = ""

# Creating Admin Panel
def admin_panel(username):
    global user_name
    user_name = username
    upper_user = user_name.upper()
    apanel = Toplevel()
    apanel.title("Welcome to Admin Panel".center(470))
    apanel.geometry("1680x1080+-10+-5")
    apanel.iconbitmap("Graphics/Logo/logo.ico")
    bg_image = Image.open("background/UserBack.png")
    apanel.bg_image_resized = bg_image.resize((1530, 880), Image.ANTIALIAS)
    apanel.resized = ImageTk.PhotoImage(apanel.bg_image_resized)
    bg_Img = Label(apanel, image=apanel.resized)
    bg_Img.place(x=0, y=0, relheight=1, relwidth=1)



    def show_data():
        bg_image = Image.open("background/UserBack.png")
        apanel.bg_image_resized = bg_image.resize((1530, 880), Image.ANTIALIAS)
        apanel.resized = ImageTk.PhotoImage(apanel.bg_image_resized)
        bg_Img = Label(apanel, image=apanel.resized)
        bg_Img.place(x=350, y=0, relheight=1, relwidth=1)

        myConn = Database()
        myCursor = myConn.mydb.cursor()

        txt_1 = Image.open("Graphics/Logo/txtfield.png")
        apanel.txt_1_resized = txt_1.resize((250, 400), Image.ANTIALIAS)
        apanel.txt1 = ImageTk.PhotoImage(apanel.txt_1_resized)

        text_input1 = Label(apanel, image=apanel.txt1, bg="#0066CA")
        text_input1.place(x=770, y=620, height=40, width=270)

        text_input_box1 = Entry(apanel, font=("Cambria", 15), bg="#E9EDF5", bd=0)
        text_input_box1.place(x=785, y=620, height=40, width=240)

        def delete():
            myConn = Database()
            myCursor = myConn.mydb.cursor()
            query = f"Delete from tbl_user where user_id ='{text_input_box1.get()}'"
            myCursor.execute(query)
            messagebox.showinfo("Delete Alert!", "Profiles Deleted Successfully.")
            myConn.mydb.commit()
            myConn.mydb.close()
            return show_data()
        myCursor.execute("Select * from tbl_user")

        tree = ttk.Treeview(apanel,selectmode='browse')
        tree.place(x=400,y=100,height=500,width = 1100)
        # Defining number of columns
        tree['columns'] =('user_id','first_name','last_name','email','gender','contact_no','password')
        tree['show'] = 'headings'

        style = ttk.Style(apanel)
        style.theme_use("clam")

        style.configure("",font=("Cambria",15))
        style.configure("Treeview.Heading", foreground="#0066CA",font=("Cambria",15,"bold"))

        tree.column("user_id", width=50, minwidth=50, anchor=CENTER)
        tree.column("first_name",width=100, minwidth= 100,anchor=CENTER)
        tree.column("last_name",width=100, minwidth= 100,anchor=CENTER)
        tree.column("email",width=100, minwidth= 100,anchor=CENTER)
        tree.column("gender",width=50, minwidth= 50,anchor=CENTER)
        tree.column("contact_no",width=100, minwidth= 100,anchor=CENTER)
        tree.column("password",width=100, minwidth= 100,anchor=CENTER)

        tree.heading("user_id",text="User Id")
        tree.heading("first_name",text="First Name")
        tree.heading("last_name",text="Last Name")
        tree.heading("email",text="Email")
        tree.heading("gender",text="Gender")
        tree.heading("contact_no", text="Contact")
        tree.heading("password", text="Password")

        i = 0
        for res in myCursor:
            tree.insert("",i,text="",values=(res[0],res[1],res[2],res[3],res[4],res[5],res[6]))
            i = i+1

        myCursor.fetchall()
        myCursor.close()
        myConn.mydb.close()

        btn_delete_img = Image.open("background/btn_delete.png")
        apanel.bg_delete_resized = btn_delete_img.resize((170, 50), Image.ANTIALIAS)
        apanel.delete = ImageTk.PhotoImage(apanel.bg_delete_resized)

        btn_delete = Button(apanel, image=apanel.delete, bd=0, command = delete,bg="#0066CA", activebackground="#0066CA")
        btn_delete.place(x=1050, y=615, height=50, width=200)

    def dash():
        time.sleep(0)
        apanel.withdraw()
        return admin_panel(upper_user)

    def logout():
        result = messagebox.askquestion("LOG OUT".center(90), "Are you sure you want to log out?", parent=apanel)
        if result == 'yes':
            return apanel.withdraw()
        else:
            return 0
    def update():
        myConn = Database()
        myCursor = myConn.mydb.cursor()
        upd_frame = Toplevel()
        upd_frame.title("Update Your Information".center(470))
        upd_frame.geometry("1680x1080+-10+-5")
        upd_frame.iconbitmap("Graphics/Logo/logo.ico")
        bg_image = Image.open("background/update.png")
        upd_frame.bg_image_resized = bg_image.resize((1530, 880), Image.ANTIALIAS)
        upd_frame.resized = ImageTk.PhotoImage(upd_frame.bg_image_resized)
        bg_Img = Label(upd_frame, image=upd_frame.resized)
        bg_Img.place(x=0, y=0, relheight=1, relwidth=1)

        txt_1 = Image.open("Graphics/Logo/txtfield.png")
        upd_frame.txt_1_resized = txt_1.resize((250, 400), Image.ANTIALIAS)
        upd_frame.txt1 = ImageTk.PhotoImage(upd_frame.txt_1_resized)

        text_input1 = Label(upd_frame, image=upd_frame.txt1, bg="#0066CA")
        text_input1.place(x=720, y=300, height=40, width=270)

        text_input_box1 = Entry(upd_frame, font=("Cambria", 15), bg="#E9EDF5", bd=0)
        text_input_box1.place(x=735, y=300, height=40, width=240)

        text_input2 = Label(upd_frame, image=upd_frame.txt1, bg="#0066CA")
        text_input2.place(x=720, y=440, height=40, width=270)

        text_input_box2 = Entry(upd_frame, font=("Cambria", 15), bg="#E9EDF5", bd=0)
        text_input_box2.place(x=735, y=440, height=40, width=240)
        text_input_box2.config(show="*")

        text_input3 = Label(upd_frame, image=upd_frame.txt1, bg="#0066CA")
        text_input3.place(x=720, y=580, height=40, width=270)

        text_input_box3 = Entry(upd_frame, font=("Cambria", 15), bg="#E9EDF5", bd=0)
        text_input_box3.place(x=735, y=580, height=40, width=240)
        text_input_box3.config(show="*")

        def cancel():
            result = messagebox.askquestion("Cancel".center(90), "Do you want to Cancel?", parent=upd_frame)
            if result == 'yes':
                return upd_frame.withdraw()
            else:
                return 0

        def change():
            apanel.withdraw()
            global user_name
            update_username = text_input_box1.get()
            update_password = text_input_box2.get()
            update_confirmpassword = text_input_box3.get()
            try:
                if update_password != update_confirmpassword:
                    messagebox.showinfo("Alert!".center(90),
                                        "Try again! Password and Re-Entered Password are Unmatched.")
                else:
                    query = f"Update admin_user Set user_name='{update_username}',password='{update_password}' where user_name = '{user_name}'"
                    myCursor.execute(query)
                    user_name = text_input_box1.get()
                    messagebox.showinfo("Update Alert!", "Username and password Updated Sucessfully")
                    upd_frame.withdraw()
                    myConn.mydb.commit()
                    myConn.mydb.close()
                    return admin_panel(user_name)
            except:
                pass

        btn_update_img = Image.open("background/btn_update.png")
        upd_frame.bg_update_resized = btn_update_img.resize((190, 60), Image.ANTIALIAS)
        upd_frame.update = ImageTk.PhotoImage(upd_frame.bg_update_resized)

        btn_cancel_img = Image.open("background/btn_cancle.png")
        upd_frame.bg_cancel_resized = btn_cancel_img.resize((190, 65), Image.ANTIALIAS)
        upd_frame.cancel = ImageTk.PhotoImage(upd_frame.bg_cancel_resized)

        btn_update = Button(upd_frame, image=upd_frame.update, bd=0, bg="#0066CA", activebackground="#0066CA",
                            command=change)
        btn_update.place(x=718, y=675, height=60, width=210)

        btn_update = Button(upd_frame, image=upd_frame.cancel, bd=0, bg="#0066CA", activebackground="#0066CA",
                            command=cancel)
        btn_update.place(x=980, y=675, height=60, width=210)

        upd_frame.mainloop()


    frame = Frame(apanel, bd=3, highlightthickness=5, highlightcolor="#1a2b63", highlightbackground="#1a2b63",
                  bg="#E9EDF5")
    frame.place(x=5, y=0, height=835, width=350)
    label = Label(apanel, text=f"WELCOME, {upper_user}", font=("Cambria", 18), fg="#0066CA", bg="#E9EDF5")
    label.place(x=70, y=200)

    user_image = ImageTk.PhotoImage(Image.open("userpanel_graphics/user_icon.png"))
    user_lbl = Label(apanel, image=user_image, bg="#E9EDF5")
    user_lbl.place(x=110, y=50)


    # Adding Demo Video and Match Board
    my_label = Label(apanel)
    my_label.place(x=390, y=35, height=370, width=650)
    player = tkvideo("Graphics/banner/intro.mp4", my_label, loop=1, size=(640, 360))
    player.play()

    match1_img = Image.open("userpanel_graphics/match.png")
    match1_resized = match1_img.resize((330, 220), Image.ANTIALIAS)
    match1_image = ImageTk.PhotoImage(match1_resized)
    match1_lbl = Label(apanel, image=match1_image, bg="#0066CA")
    match1_lbl.place(x=385, y=440, height=220, width=330)

    match2_img = Image.open("userpanel_graphics/board3.png")
    match2_resized = match2_img.resize((320, 215), Image.ANTIALIAS)
    match2_image = ImageTk.PhotoImage(match2_resized)
    match2_lbl = Label(apanel, image=match2_image, bg="#0066CA")
    match2_lbl.place(x=770, y=443, height=215, width=320)

    match3_img = Image.open("userpanel_graphics/board4.png")
    match3_resized = match3_img.resize((320, 215), Image.ANTIALIAS)
    match3_image = ImageTk.PhotoImage(match3_resized)
    match3_lbl = Label(apanel, image=match3_image, bg="#0066CA")
    match3_lbl.place(x=1150, y=443, height=215, width=320)

    pointBoard_img = Image.open("points/point_board.png")
    pointBoard_resized = pointBoard_img.resize((320, 220), Image.ANTIALIAS)
    pointBoard_image = ImageTk.PhotoImage(pointBoard_resized)
    pointBoard_lbl = Label(apanel, image=pointBoard_image, bg="#0066CA")
    pointBoard_lbl.place(x=1150, y=100, height=215, width=320)

    bottom_img = Image.open("userpanel_graphics/bottom_banner.png")
    bottom_resized = bottom_img.resize((940, 95), Image.ANTIALIAS)
    bbanner_img = ImageTk.PhotoImage(bottom_resized)
    bottom_lbl = Label(apanel, image=bbanner_img, bg="#0066CA")
    bottom_lbl.place(x=460, y=740, height=75, width=950)

    # Dashboard Button
    btn_dash = Button(apanel, text="DASHBOARD          ", command=dash, font=("Cambria", 18), fg="#0066CA",
                      bg="#E9EDF5",
                      activebackground="#E9EDF5", activeforeground="#0066CA", bd=0)
    btn_dash.place(x=81, y=295, width=230, height=60)
    dash_img = Image.open("menu_icons/1.png")
    dash_resized = dash_img.resize((50, 55), Image.ANTIALIAS)
    dash_image = ImageTk.PhotoImage(dash_resized)
    dash_lbl = Label(apanel, image=dash_image, bg="#E9EDF5")
    dash_lbl.place(x=33, y=295, height=55, width=50)

    # Manage Profiles
    profile_img = Image.open("menu_icons/6.png")
    profile_resized = profile_img.resize((50, 55), Image.ANTIALIAS)
    profile_image = ImageTk.PhotoImage(profile_resized)
    profile_btn = Button(apanel, text=" MANAGE PROFILES         ", activebackground="#E9EDF5",
                      activeforeground="#0066CA",command=show_data,font=("Cambria", 18), fg="#0066CA", bg="#E9EDF5", bd=0)
    profile_btn.place(x=99, y=360, width=250, height=60)
    profile_lbl = Label(apanel, image=profile_image, bg="#E9EDF5")
    profile_lbl.place(x=30, y=360, height=55, width=50)

    #Update my profiles button
    update_img = Image.open("menu_icons/5.png")
    update_resized = update_img.resize((50, 55), Image.ANTIALIAS)
    update_image = ImageTk.PhotoImage(update_resized)
    update_btn = Button(apanel, text="  UPDATE MY PROFILE  ", font=("Cambria", 18),
                        command = update, activebackground="#E9EDF5", activeforeground="#0066CA", fg="#0066CA", bg="#E9EDF5", bd=0)
    update_btn.place(x=90, y=430, width=250, height=60)
    update_lbl = Label(apanel, image=update_image, bg="#E9EDF5")
    update_lbl.place(x=35, y=430, height=55, width=40)



    # Log out button
    log_img = Image.open("menu_icons/7.png")
    log_resized = log_img.resize((50, 55), Image.ANTIALIAS)
    log_image = ImageTk.PhotoImage(log_resized)
    log_btn = Button(apanel, text="  LOG OUT                          ", activebackground="#E9EDF5",
                     activeforeground="#0066CA", font=("Cambria", 18), fg="#0066CA", command=logout,
                     bg="#E9EDF5", bd=0)
    log_btn.place(x=85, y=500, width=250, height=60)
    log_lbl = Label(apanel, image=log_image, bg="#E9EDF5")
    log_lbl.place(x=30, y=500, height=55, width=50)
    apanel.mainloop()

