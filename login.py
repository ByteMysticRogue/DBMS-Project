from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from utils import get_cursor, generate_md5
from table_creation import creating_table, creating_indexes, create_admin
import create_account, forgetpassword

def main():
    creating_table()
    creating_indexes()
    create_admin()

    cursor = get_cursor()

    windows = Tk()

    windows.title("Library Management System")
    windows.geometry('490x240')
    windows.resizable(0, 0)

    #forgot password
    def forgot_password():
        windows.destroy()
        forgetpassword.main()


    #Button Definition process
    def create_one():
        windows.destroy()
        create_account.main()


    def login():
        if idEntry.get() == '' or password_entry.get() == '':
            messagebox.showerror('Alert', 'Please enter both username and password!')
        else:
            # Fetch user's information
            fetch_user_query = """
                SELECT * FROM member WHERE username=?
            """
            cursor.execute(fetch_user_query, (idEntry.get(),))
            user = cursor.fetchone()

            if user is None:
                messagebox.showerror('Alert!', 'Incorrect username or password')
            else:
                # Verify the entered password against the stored hash
                stored_password_hash = user[2]
                entered_password_hash = generate_md5(password_entry.get())
                if user[-1] != variable1.get():
                    messagebox.showerror('Alert!', 'You Don\'t have Admin Previlages!')
                else:
                    if entered_password_hash == stored_password_hash:
                        messagebox.showinfo('Success', 'Login Successful')
                        idEntry.delete(0, END)
                        password_entry.delete(0, END)
                    else:
                        messagebox.showerror('Alert!', 'Incorrect password')


    variable1 = StringVar()

    #email
    def on_entry(e):
        idEntry.delete(0, END)

    def on_password(e):
        name=idEntry.get()
        if name == '':
            idEntry.insert(0,'Email')

    #password
    def on_enter(e):
        password_entry.delete(0, END)

    def on_Leave(e):
        password = password_entry.get()
        if password == '':
            password_entry.insert(0, 'password')


    #for hiding data on the entry fields by clicking on the check box
    def show():
        password_entry.configure(show='*')
        check.configure(command=hide, text='')

    def hide():
        password_entry.configure(show='')
        check.configure(command=show, text='')


    # getting data from the entry fields
    username = StringVar()
    password = StringVar()

    frame = Frame(windows, width=700, height=400, bg='white')
    frame.place(x=0, y=0)


    user_img = PhotoImage(file='./assets/usernamelogo.png')
    idlabel = Label(frame, text='Username', fg='black', image=user_img, compound=LEFT, bg='white', font=('Calibre', 14, 'bold'))
    idlabel.grid(row=1, column=0, pady=20, padx=3)



    password_img = PhotoImage(file='./assets/padlock.png')
    password_label = Label(frame, image=password_img, compound=LEFT,fg='black', bg='white', text='Password', font=('Calibre', 14, 'bold'))
    password_label.grid(row=3, column=0, pady=10, padx=3)


    idEntry = Entry(frame, width=39, bd=3)
    idEntry.grid(row=1, column=2, columnspan=2, padx=57)


    password_entry = Entry(frame, width=39, bd=3)
    password_entry.grid(row=3, column=2, columnspan=2)

    #application of erasable text on the entry fields
    idEntry.insert(0, '@gmail.com')
    idEntry.bind('<FocusIn>', on_entry)
    idEntry.bind('<FocusOut>', on_password)

    password_entry.insert(0, "password")
    password_entry.bind('<FocusIn>', on_enter)
    password_entry.bind('<FocusOut>', on_Leave)

    roles = ['Admin', 'User']

    variable1.set('Select Role')

    rolesLabelDropdown = OptionMenu(frame, variable1, *roles)
    rolesLabelDropdown.place(x=200, y=120)

    rolesLabelDropdown.config(width=8, font=('Calibre', 8, 'bold'),  fg='black')


    #btn
    login_btn = Button(frame, text='LOGIN', bg='#7f7fff', pady=10, width=23, fg='white', font=('open sans', 9, 'bold'), cursor='hand2', border=0, borderwidth=5, command=login)
    login_btn.grid(row=9,  columnspan=5, pady=30)


    dont_have_acc_Label = Label(frame, width=20, text='Don\'t have an account?', fg='black', bg='#babcbb', pady=4, font=('Calibre', 9, 'bold'))
    dont_have_acc_Label.place(y=170)

    create_new_acc = Button(frame, width=19, text='Create New Account', border=0, bg='#babcbb', cursor='hand2', fg='black', font=('Calibre', 8, 'bold'), command=create_one)
    create_new_acc.place(y=200)

    forget_pass = Button(frame, text='Forgot Password?', fg='black', border=0, cursor='hand2', bg='#babcbb', font=('Calibre', 9, 'bold'), command=forgot_password)
    forget_pass.place(x=310, y=120)


    check = Checkbutton(frame, text='', command=show, bg='white')
    check.place(x=440, y=100)

    windows.mainloop()

if __name__ == "__main__":
    main()