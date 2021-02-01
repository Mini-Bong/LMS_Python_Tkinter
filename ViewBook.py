from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

dbName = 'LMSdb'
connector = pymysql.connect(host = 'localhost', user = 'root', database = dbName)
cur = connector.cursor()

bookTable = 'books'

def View():
    window = Tk()
    window.title("Library")
    window.minsize(width = 400, height = 400)
    window.geometry("600x500")

    background_image =Image.open("image.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    imageSizeWidth = int(imageSizeWidth/5)
    imageSizeHeight = int(imageSizeHeight/5)
    
    Canvas1 = Canvas(window)
    Canvas1.config(bg = '#F8EFBA', width = imageSizeWidth, height = imageSizeHeight)
    Canvas1.pack(expand=True, fill = BOTH)

    labelframe = Frame(window, bg = 'black')
    labelframe.place(relx =0.1, rely = 0.3, relwidth = 0.8, relheight = 0.5)

    headingframe1 = Frame(window, bg = "#333945", bd = 5)
    headingframe1.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.13)

    headingframe2 = Frame(headingframe1, bg = "#EAF0F1")
    headingframe2.place(relx = 0.01, rely = 0.05, relwidth = 0.98, relheight = 0.9)

    headinglabel = Label(headingframe2, text = "VIEW BOOKs", fg = 'black')
    headinglabel.place(relx= 0.25, rely = 0.15, relwidth = 0.5, relheight = 0.5)

    y = 0.25
    Label(labelframe, text="%-10s%-30s%-20s%-30s%-20s"%('BID','Title','Subject','Author','Status'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelframe, text="----------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    getBooks = "select * from "+bookTable
    
    try:
        cur.execute(getBooks)
        connector.commit()
        for i in cur:
            Label(labelframe, text = "%-10s%-30s%-20s%-30s%-20s"%(i[0], i[1], i[2], i[3], i[4]), bg = 'black',fg = 'white').place(relx = 0.07, rely = y)
            y += 0.1
    except:
        messagebox.showinfo("Bas formate", "can't see the books")
    window.mainloop()

