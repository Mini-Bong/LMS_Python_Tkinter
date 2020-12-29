from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

dbName = 'LMSdb'
connector = pymysql.connect(host = 'localhost', user = 'root', password = '', database = dbName)
cur = connector.cursor()

bookTable = 'books'


def search():
    global Searchbtn, labelframe, lb1, en1, quitbtn, root, Canvas1
    sub = en1.get()
    Searchbtn.destroy()
    quitbtn.destroy()
    lb1.destroy()
    en1.destroy()

    labelframe = Frame(window, bg = 'black')
    labelframe.place(relx = 0.1, rely = 0.3, relwidth = 0.8, relheight = 0.5)

    y = 0.25

    Label(labelframe, text = "%-10s%-30s%-20s%-30s%-20s"%('BID', 'Title', 'Subject', 'Authon', 'Status'), bg = 'black', fg= 'white').place(relx = 0.07, rely = 0.1)
    Label(labelframe, text = "-------------------------------------------------------------------------", bg = 'black', fg=  'white').place(relx = 0.05, rely = 0.2)

    sql_query = "select * from "+bookTable+"where subject = '"+sub"'"
    




def searchBook():
    global en1, Searchbtn, lb1, labelframe, quitbtn, Canvas1, window
    window = tk.Tk()
    window.resizable(0,0) #it disable window maximizing buttom 
    window.title("Library")
    window.minsize(width =400, height = 400)
    window.geometry("600x600")
    same = True
    background_image =Image.open("image.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    imageSizeWidth = int(imageSizeWidth/5)
    imageSizeHeight = int(imageSizeHeight/5)
    background_image = background_image.resize((imageSizeWidth,imageSizeHeight),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(window)

    Canvas1.create_image(300,450,image = img) #positing of image
    Canvas1.config(bg="white",width = imageSizeWidth, height = imageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    labelframe = Frame(window, bg = 'black')
    labelframe.place(relx = 0.1, rely = 0.2, relwidth = 0.8, relheight = 0.3)

    headingframe1 = Frame(window, bg = '#333945', bd = 5)
    headingframe1.place(relx = 0.25, rely = 0.05, relwidth = 0.5, relheight = 0.13)

    headingframe2 = Frame(headingframe1, bg = '#EAF0F1')
    headingframe2.place(relx = 0.01, rely = 0.05, relwidth = 0.98, relheight = 0.9)

    headinglabel =Label(headingframe2, text = 'Search Box', fg = 'black')
    headinglabel.place(relx = 0.25, rely = 0.15, relwidth =0.5, relheight = 0.5)

    # Book id to delete
    lb1 = Label(labelframe, text = "Enter Subject", bg = 'black', fg = 'white')
    lb1.place(relx = 0.05, rely = 0.2)

    en1 = Entry(labelframe)
    en1.place(relx = 0.3, rely = 0.2, relwidth = 0.62)

    Searchbtn = Button(labelframe, text = "Search", bg = '#264348', fg = 'white', command = search)
    Searchbtn.place(relx = 0.25, rely = 0.6, relwidth = 0.25, relheight = 0.2)

    quitbtn = Button(labelframe, text = "Quit", bg = '#455A64', fg = 'white', command = window.quit)
    quitbtn.place(relx = 0.60, rely = 0.6, relwidth = 0.25, relheight = 0.2)
    window.mainloop()


searchBook()