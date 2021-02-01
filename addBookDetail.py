from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

def register_books():
    book_id = en1.get()
    title = en2.get()
    subject = en3.get()
    author = en4.get()
    status = en5.get()

    insertBookQuery = "insert into "+bookTable+" values('"+book_id+"', '"+title+"', '"+subject+"', '"+author+"', '"+status+"')"
    try:
        cur.execute(insertBookQuery)
        connector.commit()
        messagebox.showinfo("Success!", "Books added successfully")
    except Exception as e:
        print(e)
        messagebox.showinfo("Error", "Can't add data to databse")
    print(book_id)
    print(title)
    print(subject)
    print(author)
    print(status)

    en1.delete(0, END)
    en2.delete(0,END)
    en3.delete(0, END)
    en4.delete(0, END)
    en5.delete(0, END)

def addBook():
    global en1, en2, en3, en4, en5, Canvas1, connector, cur, bookTable, window
    window = Tk()
    window.title("Library")
    window.minsize(width = 400, height = 400)
    window.geometry("600x500")
    dbName = 'LMSdb'
    bookTable = 'books'
    connector = pymysql.connect(host = 'localhost', user = 'root', database=dbName)
    cur = connector.cursor()

    background_image =Image.open("image.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    imageSizeWidth = int(imageSizeWidth/5)
    imageSizeHeight = int(imageSizeHeight/5)
    background_image = background_image.resize((imageSizeWidth,imageSizeHeight),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(window)
    Canvas1.config(bg = "#74b9ff", width = imageSizeWidth, height = imageSizeHeight)
    Canvas1.pack(expand = True, fill = BOTH)
    labelframe = Frame(window, bg='black')
    labelframe.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.7)

    lb1 = Label(labelframe, text = "Book ID : ", bg = 'black', fg = 'white')
    lb1.place(relx = 0.05, rely = 0.1)
    en1 = Entry(labelframe)
    en1.place(relx = 0.3, rely = 0.1)

    lb2 = Label(labelframe, text = "Title : ", bg = 'black', fg = 'white')
    lb2.place(relx = 0.05, rely = 0.25)
    en2 = Entry(labelframe)
    en2.place(relx = 0.3, rely = 0.25, relwidth = 0.62)

    lb3 = Label(labelframe, text = "Subject : ", bg = 'black', fg = 'white')
    lb3.place(relx = 0.05, rely = 0.4)
    en3 = Entry(labelframe)
    en3.place(relx = 0.3, rely = 0.4, relwidth = 0.62)

    lb4 = Label(labelframe, text = "Author : ", bg = 'black', fg = 'white')
    lb4.place(relx = 0.05, rely = 0.55)
    en4 = Entry(labelframe)
    en4.place(relx = 0.3, rely = 0.55, relwidth = 0.62)

    lb5 = Label(labelframe, text = "Status(Avail/issued) : ", bg = 'black', fg = 'white')
    lb5.place(relx = 0.05, rely = 0.70)
    en5 = Entry(labelframe)
    en5.place(relx = 0.3, rely = 0.70, relwidth = 0.62)

    #submit Button
    submitBtn = Button(window, text = "SUBMIT", bg = "#d1ccc0", fg = 'black', command = register_books)
    submitBtn.place(relx = 0.28, rely = 0.9, relwidth = 0.18, relheight = 0.08)

    window.mainloop()