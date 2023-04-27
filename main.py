from tkinter import *
from textblob import TextBlob

def check_spelling():
    global spell
    word=entry.get()
    a =TextBlob(word)
    right=str(a.correct())
    cs = Label(screen,text="correct is: ",bg="#dae6f6",fg="#364971")
    cs.place(x=100,y=250)
    spell.config(text=right)



screen = Tk()
screen.geometry("500x400")
screen.config(background="#dae6f6")

font_tuple = ("Comic Sans MS", 20,)

lable1 = Label(relief=GROOVE,text="Spelling Checker",font=font_tuple,bd=3)
#Frame1= Frame(background="#0000FF")
#Frame1.place(x=0,y=0)
lable1.place(x=150,y=50)
spell = Label(relief=GROOVE,text="Spelling Checker",font=font_tuple,bd=3)
spell.place(x=160,y=230)
entry = Entry(screen,justify="center",width=40,bg="white",border=2)
entry.pack(pady=10)
entry.focus()
entry.place(x=125,y=125)

Button(text="CHECK",width=10,fg="white",bg="red",command=check_spelling).place(x=200,y=160)
screen.mainloop()