from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image

answer = ['A', 'D', 'A', 'B', 'C']
question = ["Question.1) Who have won most Ballon d'Or title?", "Question.2) Who is known as hand of god?",
            "Question.3) Which Country have won most world cup title?",
            "Question.4) Which Club have won most Champions League title?",
            "Question.5) Which Country have won Copa America 2020?"]


def play():
    chance = 3
    quiz_pannel = Toplevel()
    quiz_pannel.title("Play Quiz".center(450))
    quiz_pannel.geometry("1680x1080+-10+-5")
    quiz_pannel.iconbitmap("Graphics/Logo/logo.ico")
    bg_image = Image.open("background/UserBack.png")
    quiz_pannel.bg_image_resized = bg_image.resize((1530, 880), Image.ANTIALIAS)
    quiz_pannel.resized = ImageTk.PhotoImage(quiz_pannel.bg_image_resized)
    bg_Img = Label(quiz_pannel, image=quiz_pannel.resized)
    bg_Img.place(x=0, y=0, relheight=1, relwidth=1)

    value = StringVar()

    def question5():
        global chance
        bg_image = Image.open("background/UserBack.png")
        quiz_pannel.bg_image_resized = bg_image.resize((1530, 880), Image.ANTIALIAS)
        quiz_pannel.resized = ImageTk.PhotoImage(quiz_pannel.bg_image_resized)
        bg_Img = Label(quiz_pannel, image=quiz_pannel.resized)
        bg_Img.place(x=0, y=0, relheight=1, relwidth=1)
        question_title = Label(quiz_pannel, text=f"{question[4]}", font=("Cambria", 22), bg="#0066CA", fg="#E9EDF5")
        question_title.place(x=350, y=100, height=70, width=900)
        option1 = Radiobutton(quiz_pannel, text="A.Chile", bg="#0066CA", indicator=0, bd=1, variable=value,
                              value="A")
        option1.place(x=500, y=200, height=50, width=200)

        option2 = Radiobutton(quiz_pannel, text="B.Brazil", bg="#0066CA", indicator=0, variable=value,
                              value="B")
        option2.place(x=900, y=200, height=50, width=200)

        option3 = Radiobutton(quiz_pannel, text="C.Argentina", bg="#0066CA", indicator=0, variable=value,
                              value="C")
        option3.place(x=500, y=300, height=50, width=200)

        option4 = Radiobutton(quiz_pannel, text="D.Uruguay", bg="#0066CA", indicator=0, variable=value,
                              value="D")
        option4.place(x=900, y=300, height=50, width=200)

        def answer5():
            global answer
            chance = 3
            answer_option = value.get()
            print(answer_option)
            while chance > 0:
                if answer_option == answer[4]:
                    choice = messagebox.showinfo("Correct Answer", "Argentina defeated Brazil, won COPA America 2020.",
                                                 parent=quiz_pannel)
                    quiz_pannel.withdraw()
                    break
                else:
                    chance -= 1
            else:
                messagebox.showinfo("Incorrect Answer", f"Wrong Answer! Try Again", parent=quiz_pannel)

        submit_button = Button(quiz_pannel, text="Submit", bd=2, bg="Green", command=answer5)
        submit_button.place(x=680, y=500, height=60, width=150)

    def question4():
        global chance
        bg_image = Image.open("background/UserBack.png")
        quiz_pannel.bg_image_resized = bg_image.resize((1530, 880), Image.ANTIALIAS)
        quiz_pannel.resized = ImageTk.PhotoImage(quiz_pannel.bg_image_resized)
        bg_Img = Label(quiz_pannel, image=quiz_pannel.resized)
        bg_Img.place(x=0, y=0, relheight=1, relwidth=1)
        question_title = Label(quiz_pannel, text=f"{question[3]}", font=("Cambria", 22), bg="#0066CA", fg="#E9EDF5")
        question_title.place(x=350, y=100, height=70, width=900)
        option1 = Radiobutton(quiz_pannel, text="A.AC Milan", bg="#0066CA", indicator=0, bd=1, variable=value,
                              value="A")
        option1.place(x=500, y=200, height=50, width=200)

        option2 = Radiobutton(quiz_pannel, text="B.Real Madrid", bg="#0066CA", indicator=0, variable=value,
                              value="B")
        option2.place(x=900, y=200, height=50, width=200)

        option3 = Radiobutton(quiz_pannel, text="C.Manchester United", bg="#0066CA", indicator=0, variable=value,
                              value="C")
        option3.place(x=500, y=300, height=50, width=200)

        option4 = Radiobutton(quiz_pannel, text="D.FC Barcelona", bg="#0066CA", indicator=0, variable=value,
                              value="D")
        option4.place(x=900, y=300, height=50, width=200)

        def answer4():
            global answer
            chance = 3
            answer_option = value.get()
            print(answer_option)
            while chance > 0:
                if answer_option == answer[3]:
                    choice = messagebox.showinfo("Correct Answer", "Real Madrid have won 13 Champions league titles.",
                                                 parent=quiz_pannel)
                    return question5()
                else:
                    chance -= 1
            else:
                messagebox.showinfo("Incorrect Answer", f"Wrong Answer! Try Again", parent=quiz_pannel)

        submit_button = Button(quiz_pannel, text="Submit", bd=2, bg="Green", command=answer4)
        submit_button.place(x=680, y=500, height=60, width=150)

    def question3():
        global chance
        bg_image = Image.open("background/UserBack.png")
        quiz_pannel.bg_image_resized = bg_image.resize((1530, 880), Image.ANTIALIAS)
        quiz_pannel.resized = ImageTk.PhotoImage(quiz_pannel.bg_image_resized)
        bg_Img = Label(quiz_pannel, image=quiz_pannel.resized)
        bg_Img.place(x=0, y=0, relheight=1, relwidth=1)
        question_title = Label(quiz_pannel, text=f"{question[2]}", font=("Cambria", 22), bg="#0066CA", fg="#E9EDF5")
        question_title.place(x=350, y=100, height=70, width=900)
        option1 = Radiobutton(quiz_pannel, text="A.Brazil", bg="#0066CA", indicator=0, bd=1, variable=value,
                              value="A")
        option1.place(x=500, y=200, height=50, width=200)

        option2 = Radiobutton(quiz_pannel, text="B.Germany", bg="#0066CA", indicator=0, variable=value,
                              value="B")
        option2.place(x=900, y=200, height=50, width=200)

        option3 = Radiobutton(quiz_pannel, text="C.Italy", bg="#0066CA", indicator=0, variable=value,
                              value="C")
        option3.place(x=500, y=300, height=50, width=200)

        option4 = Radiobutton(quiz_pannel, text="D.Argentina", bg="#0066CA", indicator=0, variable=value,
                              value="D")
        option4.place(x=900, y=300, height=50, width=200)

        def answer3():
            global answer
            chance = 3
            answer_option = value.get()
            print(answer_option)
            while chance > 0:
                if answer_option == answer[2]:
                    choice = messagebox.showinfo("Correct Answer", "Brazil have won 5 FIFA World Cup titles",
                                                 parent=quiz_pannel)
                    return question4()
                else:
                    chance -= 1
            else:
                messagebox.showinfo("Incorrect Answer", f"Wrong Answer! Try Again", parent=quiz_pannel)

        submit_button = Button(quiz_pannel, text="Submit", bd=2, bg="Green", command=answer3)
        submit_button.place(x=680, y=500, height=60, width=150)

    def question2():
        global chance
        bg_image = Image.open("background/UserBack.png")
        quiz_pannel.bg_image_resized = bg_image.resize((1530, 880), Image.ANTIALIAS)
        quiz_pannel.resized = ImageTk.PhotoImage(quiz_pannel.bg_image_resized)
        bg_Img = Label(quiz_pannel, image=quiz_pannel.resized)
        bg_Img.place(x=0, y=0, relheight=1, relwidth=1)
        question_title = Label(quiz_pannel, text=f"{question[1]}", font=("Cambria", 22), bg="#0066CA", fg="#E9EDF5")
        question_title.place(x=350, y=100, height=70, width=900)
        option1 = Radiobutton(quiz_pannel, text="A.Cristiano Ronaldo", bg="#0066CA", indicator=0, bd=1, variable=value,
                              value="A")
        option1.place(x=500, y=200, height=50, width=200)

        option2 = Radiobutton(quiz_pannel, text="B.Lionel Messi", bg="#0066CA", indicator=0, variable=value,
                              value="B")
        option2.place(x=900, y=200, height=50, width=200)

        option3 = Radiobutton(quiz_pannel, text="C.Pele", bg="#0066CA", indicator=0, variable=value,
                              value="C")
        option3.place(x=500, y=300, height=50, width=200)

        option4 = Radiobutton(quiz_pannel, text="D.Diego Maradona", bg="#0066CA", indicator=0, variable=value,
                              value="D")
        option4.place(x=900, y=300, height=50, width=200)

        def answer2():
            global answer
            chance = 3
            answer_option = value.get()
            print(answer_option)
            while chance > 0:
                if answer_option == answer[1]:
                    choice = messagebox.showinfo("Correct Answer", "Diego Maradona is Known as Hand of God",
                                                 parent=quiz_pannel)
                    return question3()
                else:
                    chance -= 1
            else:
                messagebox.showinfo("Incorrect Answer", f"Wrong Answer! Try Again", parent=quiz_pannel)

        submit_button = Button(quiz_pannel, text="Submit", bd=2, bg="Green", command=answer2)
        submit_button.place(x=680, y=500, height=60, width=150)

    def question1():
        global chance
        bg_image = Image.open("background/UserBack.png")
        quiz_pannel.bg_image_resized = bg_image.resize((1530, 880), Image.ANTIALIAS)
        quiz_pannel.resized = ImageTk.PhotoImage(quiz_pannel.bg_image_resized)
        bg_Img = Label(quiz_pannel, image=quiz_pannel.resized)
        bg_Img.place(x=0, y=0, relheight=1, relwidth=1)
        question_title = Label(quiz_pannel, text=f"{question[0]}", font=("Cambria", 22), bg="#0066CA", fg="#E9EDF5")
        question_title.place(x=350, y=100, height=70, width=900)
        option1 = Radiobutton(quiz_pannel, text="A.Lionel Messi", bg="#0066CA", indicator=0, bd=1, variable=value,
                              value="A")
        option1.place(x=500, y=200, height=50, width=200)

        option2 = Radiobutton(quiz_pannel, text="B.Cristiano Ronaldo", bg="#0066CA", indicator=0, variable=value,
                              value="B")
        option2.place(x=900, y=200, height=50, width=200)

        option3 = Radiobutton(quiz_pannel, text="C.Michel Platini", bg="#0066CA", indicator=0, variable=value,
                              value="C")
        option3.place(x=500, y=300, height=50, width=200)

        option4 = Radiobutton(quiz_pannel, text="D.Johann Cruyff", bg="#0066CA", indicator=0, variable=value,
                              value="D")
        option4.place(x=900, y=300, height=50, width=200)

        def answer1():
            global answer
            chance = 3
            no_of_chance = 3
            answer_option = value.get()
            print(answer_option)
            while chance > 0:
                if answer_option == answer[0]:
                    messagebox.showinfo("Correct Answer", "Lional Messi have won 6 Ballon d'Or", parent=quiz_pannel)
                    return question2()
                else:
                    chance -= 1
            else:
                no_of_chance -= 1
                messagebox.showinfo("Incorrect Answer", f"Wrong Answer! Try Again", parent=quiz_pannel)

        submit_button = Button(quiz_pannel, text="Submit", bd=2, bg="Green", command=answer1)
        submit_button.place(x=680, y=500, height=60, width=150)

    start_button = Button(quiz_pannel, text="Start", bd=2, bg="Green", command=question1)
    start_button.place(x=680, y=350, height=80, width=150)

    quiz_pannel.mainloop()

