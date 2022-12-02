from tkinter  import *
import tkinter.messagebox as msg


root =Tk()
root.geometry("500x420")
root, root.resizable(width=False,height=False)



root.title("This is Tkinter")

# Labels
id=Label(text="ID : ")
id.place(x=80,y=50)
# id.pack()

fName=Label(root, text="First Name : ")
fName.place(x=80,y=100)
# fName.pack()

lName=Label(root, text="Last Name : ")
lName.place(x=80,y=150)
# lName.pack()

email=Label(root, text="Email : ")
email.place(x=80,y=200)
# email.pack()

mNo=Label(root, text="Mobile : ")
mNo.place(x=80,y=250)
# mNo.pack()


#  Textbox 
e_id=Entry()
e_id.place(x=250,y=50,)

eFname=Entry()
eFname.place(x=250,y=100)

elname=Entry()
elname.place(x=250,y=150)

eEmail=Entry()
eEmail.place(x=250,y=200)

enumber=Entry()
enumber.place(x=250,y=250)

# Button

insert =Button(text="Insert", bg='gray')
insert.place(x=80,y=300)

search=Button(text="Search", bg='grey')
search.place(x=150,y=300)

update=Button(text="Update" ,bg='grey')
update.place(x=230,y=300)

dlt=Button(text="Delete",bg='grey')
dlt.place(x=300,y=300)



 






root.mainloop()


