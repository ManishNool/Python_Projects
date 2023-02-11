#step1 - import module
from tkinter import *

#step2 - GUI interaction
window = Tk()  #calling class
window.geometry("400x400")
window.title("Standard Calculator")

#step3 - adding inputs

#entrybox
e = Entry(window, width=60, borderwidth = 5)
e.place(x =5, y=5)

def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

#Buttons
b = Button(window, text = "1", width = 12, command= lambda:click(1))
b.place(x = 10, y = 60)

b = Button(window, text = "2", width = 12, command= lambda:click(2))
b.place(x = 90, y = 60)

b = Button(window, text = "3", width = 12, command= lambda:click(3))
b.place(x = 180, y = 60)

b = Button(window, text = "4", width = 12, command= lambda:click(4))
b.place(x = 10, y = 100)

b = Button(window, text = "5", width = 12, command= lambda:click(5))
b.place(x = 90, y = 100)

b = Button(window, text = "6", width = 12, command= lambda:click(6))
b.place(x = 180, y = 100)

b = Button(window, text = "7", width = 12, command= lambda:click(7))
b.place(x = 10, y = 140)

b = Button(window, text = "8", width = 12, command= lambda:click(8))
b.place(x = 90, y = 140)

b = Button(window, text = "9", width = 12, command= lambda:click(9))
b.place(x = 180, y = 140)

b = Button(window, text = "0", width = 12, command= lambda:click(0))
b.place(x = 10, y = 180)

#operators

def add():
    n1 = e.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text = "+", width = 12, command=add)
b.place(x = 90, y = 180)

def sub():
    n1 = e.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text = "-", width = 12, command=sub)
b.place(x = 180, y = 180)

def mul():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text = "*", width = 12, command=mul)
b.place(x = 10, y = 220)

def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text = "/", width = 12, command= div)
b.place(x = 90, y = 220)

def per():
    n1 = e.get()
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text = "%", width = 12, command=per)
b.place(x = 180, y = 220)

def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0,i + int(n2))
    if math == "subtraction":
        e.insert(0,i - int(n2))
    if math == "multiplication":
        e.insert(0,i * int(n2))
    if math == "division":
        e.insert(0,i / int(n2))

b = Button(window, text = "=", width = 12, command=equal)
b.place(x = 10, y = 260)

def clear():
    e.delete(0, END)

b = Button(window, text = "Clear", width = 12, command=clear)
b.place(x = 90, y = 260)

#step4 - main loop
mainloop()