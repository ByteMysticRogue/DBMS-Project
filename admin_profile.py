from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import admin_panel
from utils import get_cursor


def main():
    windows = Tk()

    windows.title("Library Management System")
    windows.geometry('600x400')
    windows.resizable(0, 0)

    def back_to_main():
        windows.destroy()
        admin_panel.main()

    # First Frame
    frame1 = Frame(windows, width=800, height=150, bg='white')
    frame1.pack(fill=BOTH, expand=True)

    heading1 = Label(frame1, text='Library Book List', fg='black', bg='white', font=('Calibre', 20, 'bold'))
    heading1.place(x=275, y=20)

    library_Image = PhotoImage(file='./assets/library.png')
    library_Image_label = Label(frame1, image=library_Image)
    library_Image_label.place(x=240, y=20)

    bck_btn = Button(frame1, text='<<', width=7, borderwidth=5, height=2, bg='#babcbb', fg='black', cursor='hand2',
                     border=2, command=lambda: back_to_main())
    bck_btn.place(x=25, y=20)

    windows.mainloop()




if __name__ == '__main__':
    main()