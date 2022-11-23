from tkinter import *
import tkinter.messagebox as msg

root=Tk()
root.geometry("400x450")
root.minsize(200,200)
root.maxsize(600,650)
# Agr size ko fix krna ho toh resizable method ka use 
root.resizable(width=False,height=False)

root.title("Registration Form")
# Labels

lname=Label(text="Name")
lname.place(x=100,y=100)

gender=Label(text="Gender")
gender.place(x=100,y=150)

add=Label(text="Address")
add.place(x=100,y=200)

# TextBox

name=Entry()
name.place(x=200,y=100)

gender=Radiobutton()





root.mainloop()