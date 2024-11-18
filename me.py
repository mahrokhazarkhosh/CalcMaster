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

#------تابع محاسبات-----

def jam():
    label.configure(text=int(E1.get())) + int(E2.get())
def tafrigh():
    label.configure(text=int(E1.get())) - int(E2.get())
def zarb():
    label.configure(text=int(E1.get())) * int(E2.get())
def taghsim():
    label.configure(text=int(E1.get())) / int(E2.get())

#
