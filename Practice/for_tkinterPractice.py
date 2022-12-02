from tkinter import *
import tkinter.messagebox as msg

root=Tk()
root.geometry("460x520")

# root.maxsize(460,550)
# root.minsize(250,350)
root.resizable(width=False,height=False)


root.title("Tkinter Practice")


name=Label(text="Name")
name.place(x=80,y=100)
eName=Entry(root)
eName.place(x=220,y=100)


email=Label(text="Email")
email.place(x=80,y=180)

eEmail=Entry(root)
eEmail.place(x=220,y=180)



insert=Button(text='Insert')
insert.place(x=80,y=250)

search





root.mainloop()