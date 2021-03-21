import tkinter as tk
from tkinter import *
import pymysql
from PIL import ImageTk, Image
from tkinter import messagebox


dbName = "LMSdb"
empTable = "empdetail"
stuTable = "studetail"
bookTable = "books"
issueBookTable = "issueBookDetail"
count = 0
connector = pymysql.connect(host ='localhost', user = 'root', database = dbName)
cur = connector.cursor()

allRollNum = []
allEmpId = []
allBookId =[]

def issue():
    global issueBtn, labelFrame, lb1, en1, en2, en3, quitBtn, window, Canvas1, status

    book_id = en1.get()
    issue_to = en2.get()
    issue_be = en3.get()
    issueBtn.destroy()
    quitBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    en1.destroy()
    en2.destroy()
    en3.destroy()

    extract_book_id = "select bookId from "+bookTable
    try:
        cur.execute(extract_book_id)
        connector.commit()
        for i in cur:
            allBookId.append(i[0])
        if book_id in allBookId:
            checkAvail = "select status from "+bookTable+" where bookId = '"+book_id+"'"
            cur.execute(checkAvail)
            connecter.commit()
            for i in cur:
                check = i[0]
            




def issuebook():
    global en1, en2, en3, issueBtn, lb1, labelFrame, quitBtn, Canvas1, window, status
    window = Tk()
    window.title("Library")
    window.minsize(width = 400, height = 400)
    window.geometry("600x600")
    same = True
    background_image =Image.open("image.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    imageSizeWidth = int(imageSizeWidth/5)
    imageSizeHeight = int(imageSizeHeight/5)
    background_image = background_image.resize((imageSizeWidth,imageSizeHeight),Image.ANTIALIAS)

    Canvas1 = Canvas(window)
    Canvas1.config(bg="#706fd3",width = imageSizeWidth, height = imageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    labelFrame = Frame(window, bg = 'black')
    labelFrame.place(relx = 0.1, rely = 0.3, relwidth = 0.8, relheight = 0.3)

    headingframe1 = Frame(window, bg = '#333945', bd = 5)
    headingframe1.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.13)

    headingframe2 = Frame(headingframe1, bg = '#EAF0F1')
    headingframe2.place(relx = 0.01, rely = 0.05, relwidth = 0.98, relheight = 0.9)

    headingLabel = Label(headingframe2, text = 'ISSUE BOOK', fg = 'black')
    headingLabel.place(relx = 0.25, rely = 0.15, relwidth = 0.5, relheight = 0.5)

    #Book id
    lb1 = Label(labelFrame, text = 'Book Id: ', bg = 'black', fg = 'white')
    lb1.place(relx= 0.05, rely = 0.2)
    en1 = Entry(labelFrame)
    en1.place(relx = 0.3, rely = 0.2, relwidth = 0.62)

    #issue to roll number

    lb2 = Label(labelFrame, text = 'Issued to(roll number): ' ,bg ='black', fg = 'white')
    lb2.place(relx = 0.05, rely = 0.4)
    en2 = Entry(labelFrame)
    en2.place(relx = 0.3, rely = 0.4, relwidth = 0.62)

    #issue book employes number
    
    lb3 = Label(labelFrame, text = "Issued by(EmailId): ", bg = 'black', fg = 'white')
    lb3.place(relx = 0.05, rely = 0.6)
    en3 = Entry(labelFrame)
    en3.place(relx = 0.3, rely = 0.6, relwidth = 0.62)

    #Issue button
    issueBtn = Button(window, text = 'Issue', bg = '#d1ccc0', fg = 'black', command = issue)
    issueBtn.place(relx = 0.28, rely = 0.75, relwidth = 0.18, relheight = 0.08)

    #quit button
    quitBtn = Button(window, text = 'Quit', bg = '#aaa69d', fg = 'black', command = window.quit)
    quitBtn.place(relx =0.53, rely = 0.75, relwidth = 0.18, relheight = 0.08)

issuebook()
window.mainloop()