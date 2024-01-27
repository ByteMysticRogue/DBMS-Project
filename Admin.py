from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
from utils import get_cursor

def main():
    windows = Tk()

    windows.title("Library Management System")
    windows.geometry('600x400')
    windows.resizable(0, 0)

    def bookList():
        return None

    frame = Frame(windows, width=700, height=500, bg='white')
    frame.place(x=0, y=0)

    heading = Label(frame, text='Library Admin Panel', fg='black', bg='white', font=('Calibre', 20, 'bold'))
    heading.place(x=175, y=20)

    library_Image = PhotoImage(file='./assets/library.png')
    library_Image_label = Label(frame, image=library_Image)
    library_Image_label.place(x=125, y=20)

    book_list_btn = Button(frame, text='Book List', width=15, borderwidth=5, height=2, bg='#7f7fff', fg='white', cursor='hand2',
                           border=2, font=('#57a1f8', 16, 'bold'), command=bookList)
    book_list_btn.place(x=50, y=90)

    see_profile_btn = Button(frame, text='Profile', width=15, borderwidth=5, height=2, bg='#7f7fff', fg='white', cursor='hand2',
                             border=2, font=('#57a1f8', 16, 'bold'), command=bookList())
    see_profile_btn.place(x=350, y=90)

    list_of_users_btn = Button(frame, text='User List', width=15, borderwidth=5, height=2, bg='#7f7fff', fg='white', cursor='hand2',
                               border=2, font=('#57a1f8', 16, 'bold'), command=bookList())
    list_of_users_btn.place(x=50, y=180)

    suspend_btn = Button(frame, text='Suspend User', width=15, borderwidth=5, height=2, bg='#7f7fff', fg='white', cursor='hand2',
                               border=2, font=('#57a1f8', 16, 'bold'), command=bookList())
    suspend_btn.place(x=50, y=280)

    add_book_btn = Button(frame, text='Add Book', width=15, borderwidth=5, height=2, bg='#7f7fff', fg='white', cursor='hand2',
                          border=2, font=('#57a1f8', 16, 'bold'), command=bookList())
    add_book_btn.place(x=350, y=180)

    remove_btn = Button(frame, text='Remove Book', width=15, borderwidth=5, height=2, bg='#7f7fff', fg='white', cursor='hand2',
                          border=2, font=('#57a1f8', 16, 'bold'), command=bookList())
    remove_btn.place(x=350, y=280)


    windows.mainloop()

if __name__ == '__main__':
    main()