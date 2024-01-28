from tkinter import *
from PIL import Image, ImageTk
from utils import get_cursor
import booklist, admin_profile

def main():
    windows = Tk()

    windows.title("Library Management System")
    windows.geometry('600x500')
    windows.resizable(0, 0)

    def show_book_list():
        windows.destroy()
        booklist.main()

    def profile():
        windows.destroy()
        admin_profile.main()

    frame = Frame(windows, width=700, height=500, bg='white')
    frame.place(x=0, y=0)

    heading = Label(frame, text='Library Admin Panel', fg='black', bg='white', font=('Calibre', 20, 'bold'))
    heading.place(x=175, y=20)

    lib_Image = PhotoImage(file='./assets/library.png')
    library_Image_label = Label(frame, image=lib_Image)
    library_Image_label.place(x=125, y=20)

    book_list_btn = Button(frame, text='Book List', width=15, borderwidth=5, height=2, bg='#7f7fff', fg='white', cursor='hand2',
                           border=2, font=('#57a1f8', 16, 'bold'), command=lambda: show_book_list())
    book_list_btn.place(x=50, y=90)

    see_profile_btn = Button(frame, text='Profile', width=15, borderwidth=5, height=2, bg='#7f7fff', fg='white', cursor='hand2',
                             border=2, font=('#57a1f8', 16, 'bold'), command=lambda: profile())
    see_profile_btn.place(x=350, y=90)

    list_of_users_btn = Button(frame, text='User List', width=15, borderwidth=5, height=2, bg='#7f7fff', fg='white', cursor='hand2',
                               border=2, font=('#57a1f8', 16, 'bold'), command=show_book_list)
    list_of_users_btn.place(x=50, y=180)

    suspend_btn = Button(frame, text='Suspend User', width=15, borderwidth=5, height=2, bg='#7f7fff', fg='white', cursor='hand2',
                               border=2, font=('#57a1f8', 16, 'bold'), command=show_book_list)
    suspend_btn.place(x=50, y=280)

    add_book_btn = Button(frame, text='Add Book', width=15, borderwidth=5, height=2, bg='#7f7fff', fg='white', cursor='hand2',
                          border=2, font=('#57a1f8', 16, 'bold'), command=show_book_list)
    add_book_btn.place(x=350, y=180)

    remove_btn = Button(frame, text='Remove Book', width=15, borderwidth=5, height=2, bg='#7f7fff', fg='white', cursor='hand2',
                          border=2, font=('#57a1f8', 16, 'bold'), command=show_book_list)
    remove_btn.place(x=350, y=280)

    windows.mainloop()

if __name__ == '__main__':
    main()
