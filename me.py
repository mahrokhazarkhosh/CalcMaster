#-----بار گذاری کتابخونه----

import tkinter

#-----ایجاد پنجره------

win = tkinter.Tk()
win.title("Calculator")
win.geometry("500x300")

#------lbl-----

label = tkinter.Label(win, text="Calculator")
label.pack()
E1 = tkinter.Entry(win)
E1.pack()
E2 = tkinter.Entry(win)
E2.pack()

#