from tkinter import *
import tkinter.messagebox as msg

import mysql.connector


def createConnection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="emp"

    )


print(createConnection())


def for_insert():
    if eFname.get() == '' or elname.get() == '' or eEmail.get() == '' or enumber.get() == '':
        # print("Data mandatory")
        msg.showinfo(" ", "All Data is mandatory")
    else:
        con = createConnection()
        # con.open()
        cursor = con.cursor()
        query = "insert into emp_nfo(fname,lname,email,mobile) values(%s,%s,%s,%s)"
        args = (eFname.get(), elname.get(), eEmail.get(), enumber.get())
        cursor.execute(query, args)
        con.commit()
        con.close()

        eFname.delete(0, 'end')
        elname.delete(0, 'end')
        eEmail.delete(0, 'end')
        enumber.delete(0, 'end')
        msg.showinfo(" ", "Data Inserted successfully")


def for_search():
    eFname.delete(0, 'end')
    elname.delete(0, 'end')
    eEmail.delete(0, 'end')
    enumber.delete(0, 'end')
    if e_id.get() == '':
        msg.showinfo("", "Id  is mandatory for search any data")
    else:
        con = createConnection()
        cursor = con.cursor()
        query = "select * from emp_nfo where id=%s"
        args = (e_id.get(),)
        cursor.execute(query, args)
        row = cursor.fetchall()
        if row:
            for i in row:
                eFname.insert(0, i[1])
                elname.insert(0, i[2])
                eEmail.insert(0, i[3])
                enumber.insert(0, i[4])
        else:
            msg.showinfo("", "Id not found")

        con.commit()
        con.close()


def for_update():
    if e_id.get() == '':
        msg.showinfo("", "Id is mandatory")
    else:
        con = createConnection()
        cursor = con.cursor()
        query = "update emp_nfo set fname=%s,lname=%s, email =%s,mobile=%s where id=%s"
        args = (eFname.get(),elname.get(),eEmail.get(),enumber.get(),e_id.get())
        cursor.execute(query,args)
        con.commit()
        con.close()

        e_id.delete(0,'end')
        eFname.delete(0,'end')
        elname.delete(0,'end')
        eEmail.delete(0,'end')
        enumber.delete(0,'end')

        msg.showinfo("","Updated successfully ")


def for_dlt():
    if e_id.get()=="":
        msg.showinfo("","Is is Mandatory")
    else:
        con=createConnection()
        cursor=con.cursor()
        query="delete from emp_nfo where id=%s "
        args=(e_id.get(),)
        cursor.execute(query,args)
        con.commit()
        con.close()


        e_id.delete(0,'end')
        eFname.delete(0,'end')
        elname.delete(0,'end')
        eEmail.delete(0,'end')
        enumber.delete(0,'end')

        msg.showinfo("","Deleted operation successful")





root = Tk()
root.geometry("500x420")
root, root.resizable(width=False, height=False)


root.title("This is Tkinter")

# Labels
id = Label(text="ID : ")
id.place(x=80, y=50)
# id.pack()

fName = Label(root, text="First Name : ")
fName.place(x=80, y=100)
# fName.pack()

lName = Label(root, text="Last Name : ")
lName.place(x=80, y=150)
# lName.pack()

email = Label(root, text="Email : ")
email.place(x=80, y=200)
# email.pack()

mNo = Label(root, text="Mobile : ")
mNo.place(x=80, y=250)
# mNo.pack()


#  Textbox
e_id = Entry()
e_id.place(x=250, y=50,)

eFname = Entry()
eFname.place(x=250, y=100)

elname = Entry()
elname.place(x=250, y=150)

eEmail = Entry()
eEmail.place(x=250, y=200)

enumber = Entry()
enumber.place(x=250, y=250)

# Button

insert = Button(text="Insert", bg='gray', command=for_insert)
insert.place(x=80, y=300)

search = Button(text="Search", bg='grey', command=for_search)
search.place(x=150, y=300)

update = Button(text="Update", bg='grey', command=for_update)
update.place(x=230, y=300)

dlt = Button(text="Delete", bg='grey',command=for_dlt)
dlt.place(x=300, y=300)


root.mainloop()
