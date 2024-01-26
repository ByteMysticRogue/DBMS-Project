from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
from utils import get_cursor, generate_md5

cursor = get_cursor()

windows = Tk()
windows.geometry('500x460')
windows.resizable(0, 0)
windows.title("Library Management System")

def back():
    windows.destroy()
    import login

def submit():
    try:
         if usernameEntry.get() == '' or emailEntry.get() == '' or NewpasswordEntry.get() == '' or confirmpasswordEntry.get() == '':
             messagebox.showerror('Error', "Entry fields must be entered")
             return

         elif NewpasswordEntry.get() != confirmpasswordEntry.get():
             messagebox.showerror('Error', "Passwords don't match")
             return
         else:
             searching_user_query = """
                      SELECT * FROM member WHERE username=? AND email=?
             """
             cursor.execute(searching_user_query, (usernameEntry.get(), emailEntry.get()))
             user = cursor.fetchone()

             if user is None:
                 messagebox.showerror('Error', 'Incorrect email or password')
             else:
                 update_password = """
                        UPDATE member SET password=? WHERE username=? AND email=?
                 """
                 cursor.execute(update_password, (generate_md5(NewpasswordEntry.get()), usernameEntry.get(), emailEntry.get()))
                 cursor.commit()
                 cursor.close()
                 messagebox.showinfo('Success', 'Succesful Changes please login with New password')

                 windows.destroy()

                 import login
    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {str(e)}')


frame = Frame(windows, width=540, height=640, bg='white', bd=8)
frame.place(x=0,y=0)

#labels on window
heading = Label(frame, text='FORGET PASSWORD', fg='black', bg='white', font=('Calibre', 20, 'bold'))
heading.place(x=110, y=15)

usernameImage = PhotoImage(file='./assets/padlock.png')
usernameLabel = Label(frame, image=usernameImage)
usernameLabel.place(x=45, y=15)

usernamelbl = Label(frame, text='Username:', fg='black', bg='white', font=('Calibre', 15, 'bold'))
usernamelbl.place(x=10, y=100)

usernameEntry = Entry(frame, width=30, borderwidth=2)
usernameEntry.place(x=250, y=100)

emaillbl = Label(frame, text='Email:', fg='black', bg='white', font=('Calibre', 15, 'bold'))
emaillbl.place(x=10, y=150)

emailEntry=Entry(frame, width=30, borderwidth=2)
emailEntry.place(x=250, y=150)

Newpasswordlbl = Label(frame, text='New Password:', fg='black', bg='white', font=('Calibre', 15, 'bold'))
Newpasswordlbl.place(x=10, y=200)

NewpasswordEntry=Entry(frame, width=30, borderwidth=2)
NewpasswordEntry.place(x=250, y=200)

confirmPasswordlbl = Label(frame, text='Confirm New Password:', fg='black', bg='white', font=('Calibre', 15, 'bold'))
confirmPasswordlbl.place(x=10, y=250)

confirmpasswordEntry=Entry(frame, width=30, borderwidth=2)
confirmpasswordEntry.place(x=250, y=250)

submit1btn = Button(frame, text='Submit', width=15, height=2, bg='#7f7fff', fg='white', cursor='hand2', border=2, borderwidth=5, font=('#57a1f8', 16, 'bold'), command=submit)
submit1btn.place(x=130, y=300)

bckbtn = Button(frame, text='<<', width=7, borderwidth=5, height=2, bg='white', fg='black', cursor='hand2', border=2,
                command=back)
bckbtn.place(x=10, y=400)

windows.mainloop()