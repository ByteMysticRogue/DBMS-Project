from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import login
from utils import get_cursor, generate_md5, email_validation, phone_number_validation

def main():
    cursor = get_cursor()

    windows = Tk()
    windows.geometry('540x640')
    windows.resizable(0, 0)

    windows.title("Library Management System")


    #show and hide password
    def show():
        password_Entry.configure(show='#')
        check1.configure(command=hide)

    def hide():
        password_Entry.configure(show='')
        check1.configure(command=show)


    def show1():
            re_enter_password_Entry.configure(show='#')
            check2.configure(command=hide1)

    def hide1():
            re_enter_password_Entry.configure(show='')
            check2.configure(command=show1)


    def back():
        windows.destroy()
        login.main()


    def submit():

        if firstname_Entry.get()=='' or lastname_Entry.get()=='' or email_entry.get()=='' \
                or username_Entry.get()=='' or password_Entry.get()=='' or \
                re_enter_password_Entry.get()=='':
                messagebox.showerror('Alert!', 'All Fields must be entered') #this is to check if all the entry fields are
                # empty if it is true it'll show a msgbox error

        elif password_Entry.get() != re_enter_password_Entry.get():
            messagebox.showerror('Alert!', 'Passwords didn\'t Match')

        elif not email_validation(email_entry.get()) or not phone_number_validation(phone_num_entry.get()):
            messagebox.showerror('Alert!', 'Email Address Or Phone Number Are not valid!')

        else:
            try:
                insert_user_to_db = """
                    INSERT INTO member (username,password,first_name,last_name,email,address,phone)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """
                cursor.execute(insert_user_to_db, (username_Entry.get(), generate_md5(password_Entry.get()), firstname_Entry.get(), lastname_Entry.get(), \
                                                   email_entry.get(), address_entry.get(), phone_num_entry.get()))
                cursor.commit()
                cursor.close()
                messagebox.showinfo('Success', 'Successful Registration.')
            except Exception as e:
                print(f"Error: {e}")

            # to clear the fields after a successful registration
            firstname_Entry.delete(0, END)
            lastname_Entry.delete(0, END)
            address_entry.delete(0, END)
            phone_num_entry.delete(0, END)
            email_entry.delete(0, END)
            username_Entry.delete(0, END)
            password_Entry.delete(0, END)
            re_enter_password_Entry.delete(0, END)


    # getting data from the entry fields
    firstname = StringVar()
    lastname = StringVar()
    email = StringVar()
    username = StringVar()
    password = StringVar()
    phone = StringVar()
    Address = StringVar()

    # frame=Frame(windows)
    frame = Frame(windows, width=610, height=640, bg='white', bd=8)
    frame.place(x=0, y=0)


    #labels on window
    heading = Label(frame, text='Library Registration Form', fg='black', bg='white', font=('Calibre', 20, 'bold'))
    heading.place(x=90, y=20)


    username_Image = PhotoImage(file='./assets/usernamelogo.png')
    username_Label = Label(frame, image=username_Image)
    username_Label.place(x=45, y=20)

    firstname_Label = Label(frame, text="First Name:", fg='black', bg='white', font=('Calibre', 15, 'bold'))
    firstname_Label.place(x=10, y=100)

    firstname_Entry = Entry(frame, width=30, borderwidth=2)
    firstname_Entry.place(x=240, y=100)


    lastname_Label = Label(frame, text="Last Name:", fg='black',bg='white', font=('Calibre', 15, 'bold'))
    lastname_Label.place(x=10, y=150)

    lastname_Entry = Entry(frame, width=30, borderwidth=2)
    lastname_Entry.place(x=240, y=150)

    address_label = Label(frame, text='Address:', fg='black', bg='white', font=('Calibre', 15, 'bold'))
    address_label.place(x=10, y=200)

    address_entry = Entry(frame, width=30, borderwidth=2)
    address_entry.place(x=240, y=200)

    idlabel_Email = Label(frame, text='Email:', fg='black', bg='white', font=('Calibre', 15, 'bold'))
    idlabel_Email.place(x=10, y=250)

    email_entry = Entry(frame, width=30, borderwidth=2)
    email_entry.place(x=240, y=250)

    phone_num_label = Label(frame, text='Phone:', fg='black', bg='white', font=('Calibre', 15, 'bold'))
    phone_num_label.place(x=10, y=300)

    phone_num_entry = Entry(frame, width=30, borderwidth=2)
    phone_num_entry.place(x=240, y=300)

    username_lbl = Label(frame, text='Username:', fg='black', bg='white', font=('Calibre', 15, 'bold'))
    username_lbl.place(x=10, y=350)

    username_Entry = Entry(frame, width=30, borderwidth=2)
    username_Entry.place(x=240, y=350)

    password_lbl = Label(frame, text='Password:', fg='black', bg='white', font=('Calibre', 15, 'bold'))
    password_lbl.place(x=10, y=400)

    password_Entry=Entry(frame, width=30, borderwidth=2)
    password_Entry.place(x=240, y=400)

    re_enter_password_lbl = Label(frame, text='Confirm Password:', fg='black', bg='white', font=('Calibre', 15, 'bold'))
    re_enter_password_lbl.place(x=10, y=450)

    re_enter_password_Entry = Entry(frame, width=30, borderwidth=2)
    re_enter_password_Entry.place(x=240, y=450)

    bck_btn = Button(frame, text='<<', width=7, borderwidth=5, height=2, bg='#babcbb', fg='black', cursor='hand2', border=2,
                    command=back)
    bck_btn.place(x=10, y=580)

    submit1btn = Button(frame, text='Submit', width=15, borderwidth=5, height=2, bg='#7f7fff', fg='white', cursor='hand2',
                        border=2,font=('#57a1f8', 16, 'bold'), command=submit)
    submit1btn.place(x=150, y=500)

    #to show and hide password
    check1 = Checkbutton(frame, text='',
            command=show, bg='white')
    check1.place(x=420, y=350)

    check2 = Checkbutton(frame, text='',
            command=show1, bg='white')
    check2.place(x=420, y=400)


    windows.mainloop()

if __name__ == '__main__':
    main()