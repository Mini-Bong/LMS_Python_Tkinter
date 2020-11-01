import tkinter as tk
from tkinter import *
import pymysql
from PIL import ImageTk, Image
from tkinter import messagebox
from addBookDetail import *

dbName = "LMSdb"
empTable = "empdetail"
stuTable = "studetail"
window = tk.Tk()
window.resizable(0,0) #it disable window maximizing buttom
window.title("Library Management System")
window.minsize(width =400, height = 400)
window.geometry("600x600")
count = 0
connector = pymysql.connect(host ='localhost', user = 'root', database = dbName)
cur = connector.cursor()
def empMenu():
    print('empMenu')
    global headingframe1, headingframe2, LabelFrame, headleble1, submitBtn, Canvas1, backbtn
    headleble1.destroy()
    headingframe2.destroy()
    headingframe1.destroy()
    Canvas1.destroy()
    submitBtn.destroy()
    Canvas1 = Canvas(window)
    Canvas1.config(bg= '#F7F1E3', width = imageSizeWidth, height = imageSizeHeight)
    Canvas1.pack(expand=True, fill= BOTH)

    headingframe1 = Frame(window, bg='#333945', bd = 5)
    headingframe1.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.13)

    headingframe2 = Frame(headingframe1, bg = "#EAF0F1")
    headingframe2.place(relx =0.01, rely = 0.05, relwidth = 0.98, relheight = 0.9)

    headleble1 = Label(headingframe2, text = "Employee Menu", fg ='black')
    headleble1.place(relx = 0.25, rely = 0.15, relwidth = 0.5, relheight = 0.5)
    Btn1 = Button(window, text = "Add Book Details", bg = 'black', fg = 'white', command = addBook)
    Btn1.place(relx = 0.28, rely = 0.3, relwidth = 0.45, relheight = 0.1)

    Btn2 = Button(window, text = "Delete Book", bg = 'black', fg = 'white', command = delete)
    Btn2.place(relx = 0.28, rely = 0.4, relwidth = 0.45, relheight = 0.1)

    Btn3 = Button(window, text = "View Book List", bg ='black', fg = 'white', command= View)
    Btn3.place(relx = 0.28, rely = 0.5, relwidth = 0.45, relheight = 0.1)

    Btn4 = Button(window, text = "Search Book", bg = 'black', fg = 'white', command = searchbook)
    Btn4.place(relx = 0.28, rely = 0.6, relwidth = 0.45, relheight =  0.1)

    Btn5 = Button(window, text ="Issue Book to student", bg = 'black', fg= 'white', command = issuebook)
    Btn5.place(relx = 0.28, rely = 0.7, relwidth = 0.45, relheight = 0.1)

    backbtn = Button(window, text ="<  Back", bg = '#455A64', fg = 'white', command = Employee)
    backbtn.place(relx = 0.5, rely = 0.9, relwidth = 0.18, relheight = 0.08)


def studentMenu():
    print('Student menu')

def gettingLoginDetail():
    id = en1.get()
    password = en2.get()
    role = en3.get()
    flag1 = False
    flag2 = False
    try:
        id = int(id)
    except:
        messagebox.showinfo("ERROR", "Id should be integer")
        return
    if role == 'emp':
        sqlLoginID = "select empId from "+empTable
        cur.execute(sqlLoginID)
        names = list(cur.fetchall())
        for i in names:
            for j in list(i):
                if id == int(j):
                    flag1 = True
                    break
        if flag1 == False:
            messagebox.showerror("Failure", "Incorrect login ID")
            return
        sqlpass = "select password from "+empTable
        cur.execute(sqlpass)
        myresult = list(cur.fetchall())
        for i in myresult:
            for j in list(i):
                if password == j:
                    flag2 = True
                    break
        if flag2 == False:
            messagebox.showerror("Failure", "Incorrect Password")
            return
        if flag1 == True and flag2 == True:
            empMenu()
            messagebox.showinfo("SUCCESS","You have successfully logged in")
        else:
            messagebox.showinfo("Warning", "User doesn't Exist")
    elif role == 'stu':
        sqlLoginID = "select Roll_Num from "+stuTable
        cur.execute(sqlLoginID)
        names = list(cur.fetchall())
        for i in names:
            for j in list(i):
                if id == int(j):
                    flag1 = True
                    break
        if flag1 == False:
            messagebox.showerror("Failure", "Incorrect login ID")
            return
        sqlpass = "select password from "+stuTable
        cur.execute(sqlpass)
        myresult = list(cur.fetchall())
        for i in myresult:
            for j in list(i):
                if password == j:
                    flag2 = True
                    break
        if flag2 == False:
            messagebox.showerror("Failure", "Incorrect Password")
            return
        if flag1 == True and flag2 == True:
            studentMenu()
            messagebox.showinfo("SUCCESS","You have successfully logged in")
        else:
            messagebox.showinfo("Warning", "User doesn't Exist")

    else:
        messagebox.showwarning("Mismatch", "Enter correct Role")   
def Login():
    global LabelFrame
    global count
    count += 1
    if count>=2:
        LabelFrame.destroy()
    global en1, en2, en3, en4, submitBtn, Btn1, Btn2
    LabelFrame = Frame(window, bg = "#044F67")
    LabelFrame.place(relx = 0.2, rely = 0.44, relwidth = 0.6, relheight = 0.3)
    #Login Id BOX
    lb1 = Label(LabelFrame, text = "Login Id: ", bg="#044F67")
    lb1.place(relx = 0.05, rely = 0.1)
    en1 = Entry(LabelFrame)
    en1.place(relx = 0.3, rely = 0.1, relwidth = 0.62)

    # password
    lb2 = Label(LabelFrame, text = "Password: ", bg= "#044F67")
    lb2.place(relx = 0.05, rely = 0.4)
    en2 = Entry(LabelFrame, show='*')
    en2.place(relx = 0.3, rely = 0.4, relwidth = 0.62)

    # Role
    lb3 = Label(LabelFrame, text = "Role: ", bg = "#044F67")
    lb3.place(relx = 0.05, rely = 0.7)
    en3 = Entry(LabelFrame)
    en3.place(relx = 0.3, rely = 0.7, relwidth = 0.62)
    en3.insert(0, "emp/stu")

    # Submit Button
    submitBtn = Button(window, text = "Submit", bg = "#264328", fg = 'white', command = gettingLoginDetail)
    submitBtn.place(relx = 0.28, rely = 0.9, relwidth = 0.18, relheight = 0.08)

def gettingEmpDetail():
    empId = en1.get()
    name = en2.get()
    password = en3.get()
    department = en4.get()
    doj = en5.get()
    salary = en6.get()
    try:
        if (type(int(empId))==int):
            pass
        else:
            messagebox.showinfo("Invalid Value","Employee ID should be integer")
            return
    except:
        messagebox.showinfo("invalid Value", "Employee Id should be Integer")
        return
    try:
        if(type(float(salary))==float or type(int(salary))==int):
            pass
        else:
            messagebox.showinfo("Invalid Value", "Salary should be a float/int value")
            return
    except:
        messagebox.showinfo("Invalid Valud","Salary should be a flaot/int value")
        return
    sql = "insert into "+empTable+" values ('"+empId+"','"+name+"','"+password+"','"+department+"','"+doj+"','"+salary+"')"
    try:
        cur.execute(sql)
        connector.commit()
    except:
        messagebox.showinfo("Error inserting", "Cannot add data to database")
    en1.delete(0,END)
    en2.delete(0,END)
    en3.delete(0,END)
    en4.delete(0,END)
    en5.delete(0,END)
    en6.delete(0,END)
def EmpRegister():
    global LabelFrame
    global count
    count += 1
    if(count>=2):
        LabelFrame.destroy()
    global en1, en2, en3, en4, en5, en6
    LabelFrame = Frame(window, bg = "#044F67")
    LabelFrame.place(relx = 0.2, rely = 0.44, relwidth = 0.6, relheight = 0.42)
    #Employee ID
    lb1 = Label(LabelFrame, text = "Emp Id: ", bg = '#044F67')
    lb1.place(relx = 0.05, rely = 0.05)
    en1 = Entry(LabelFrame)
    en1.place(relx = 0.3, rely = 0.05, relwidth = 0.62)

    #Employee Name
    lb2 = Label(LabelFrame, text = "Name: ", bg = '#044F67')
    lb2.place(relx = 0.05, rely = 0.2)
    en2 = Entry(LabelFrame)
    en2.place(relx = 0.3, rely = 0.2, relwidth = 0.62)

    #Employee Password
    lb3 = Label(LabelFrame, text = "Password: ", bg = '#044F67')
    lb3.place(relx = 0.05, rely = 0.35)
    en3 = Entry(LabelFrame, show = "*")
    en3.place(relx = 0.3, rely = 0.35, relwidth = 0.62)

    #Employee Department
    lb4 = Label(LabelFrame, text = "Department: ", bg = "#044F67")
    lb4.place(relx = 0.05, rely = 0.5)
    en4 = Entry(LabelFrame)
    en4.place(relx = 0.3, rely = 0.5, relwidth = 0.62)

    #Employee Date of Joining 
    lb5 = Label(LabelFrame, text = "DOJ: ", bg = "#044F67")
    lb5.place(relx = 0.05, rely = 0.65)
    en5 = Entry(LabelFrame)
    en5.place(relx = 0.3, rely = 0.65, relwidth = 0.62)

    #Employee salary
    lb6 = Label(LabelFrame, text = "Salary: ", bg = "#044F67")
    lb6.place(relx = 0.05, rely = 0.80)
    en6 = Entry(LabelFrame)
    en6.place(relx = 0.3, rely = 0.80, relwidth = 0.62)

    #Submit Button
    SubmitBtn = Button(window, text = "SUBMIT", bg = '#264348', fg = 'white', command = gettingEmpDetail)
    SubmitBtn.place(relx = 0.28, rely = 0.9, relwidth = 0.18, relheight= 0.08)

def Employee():
    global headingframe1, headingframe2, Btn1, Btn2, headleble1, Canvas1
    headingframe1.destroy()
    headingframe2.destroy()
    Btn1.destroy()
    Btn2.destroy()
    Canvas1.destroy()
    headleble1.destroy()
    
    Canvas1 = Canvas(window)
    Canvas1.config(bg="#FFF9C4", width = imageSizeWidth, height = imageSizeHeight)
    Canvas1.pack(expand=True, fill=BOTH)

    headingframe1 = Frame(window, bg ="#333945", bd =5)
    headingframe1.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.13)

    headingframe2 = Frame(headingframe1, bg = "#EAF0F1")
    headingframe2.place(relx= 0.01, rely = 0.05, relwidth = 0.98, relheight = 0.9)

    headleble1 = Label(headingframe2, text = "Hello, Employee", fg = 'black')
    headleble1.place(relx = 0.25, rely=0.15, relwidth = 0.5, relheight = 0.5)

    Btn1 = Button(window, text = "Register", bg = 'black', fg = 'white', command = EmpRegister)
    Btn1.place(relx = 0.28, rely = 0.3, relwidth= 0.2, relheight = 0.1)

    Btn2 = Button(window, text = "Login", bg= 'black', fg = 'white', command = Login)
    Btn2.place(relx = 0.53, rely = 0.3, relwidth = 0.2, relheight = 0.1)

    Btn3 = Button(window, text = "Quit", bg = 'red', fg = 'white', command = window.quit)
    Btn3.place(relx = 0.53, rely = 0.9, relwidth = 0.18, relheight = 0.08)



def gettingStuDetail():
    rollNum = en1.get()
    name = en2.get()
    password = en3.get()
    department = en4.get()
    sem = en5.get()
    batch = en6.get()
    try:
        if(type(int(rollNum))==int):
            pass
        else:
            messagebox.showinfo("Invalid Input", "Roll Number should be integer")
            return
    except:
        messagebox.showinfo("Invalid Input", "Roll Number should be integer")
        return
    sql = "insert into "+stuTable+" values ('"+rollNum+"','"+name+"','"+password+"','"+department+"','"+sem+"','"+batch+"')"
    try:
        cur.execute(sql)
        connector.commit()
    except:
        messagebox.showinfo("Error inserting", "Cannot add data to Database")
    en1.delete(0,END)
    en2.delete(0,END)
    en3.delete(0,END)
    en4.delete(0,END)
    en5.delete(0,END)
    en6.delete(0,END)
def StuRegister():
    # roll number, student name, student password, student department, student semester, student batch
    global LabelFrame
    global count
    count += 1
    if count>=2:
        LabelFrame.destroy()
    global en1, en2, en3, en4, en5, en6
    LabelFrame = Frame(window, bg = "#044F67")
    LabelFrame.place(relx = 0.2, rely = 0.44, relwidth = 0.6, relheight = 0.42)

    #Student roll Number
    lb1 = Label(LabelFrame, text = "Roll Num: ", bg = '#044F67')
    lb1.place(relx = 0.05, rely = 0.05)
    en1 = Entry(LabelFrame)
    en1.place(relx = 0.3, rely = 0.05, relwidth = 0.62)

    #Student Name
    lb2 = Label(LabelFrame, text = "Name: ", bg = '#044F67')
    lb2.place(relx = 0.05, rely = 0.2)
    en2 = Entry(LabelFrame)
    en2.place(relx = 0.3, rely = 0.2, relwidth = 0.62)

    #Student Password
    lb3 = Label(LabelFrame, text = "Password: ", bg = '#044F67')
    lb3.place(relx = 0.05, rely = 0.35)
    en3 = Entry(LabelFrame, show = "*")
    en3.place(relx = 0.3, rely = 0.35, relwidth = 0.62)

    #Student Department
    lb4 = Label(LabelFrame, text = "Department: ", bg = "#044F67")
    lb4.place(relx = 0.05, rely = 0.5)
    en4 = Entry(LabelFrame)
    en4.place(relx = 0.3, rely = 0.5, relwidth = 0.62)

    #Student Semester
    lb5 = Label(LabelFrame, text = "Semester: ", bg = "#044F67")
    lb5.place(relx = 0.05, rely = 0.65)
    en5 = Entry(LabelFrame)
    en5.place(relx = 0.3, rely = 0.65, relwidth = 0.62)

    #Student Batch
    lb6 = Label(LabelFrame, text = "Batch: ", bg = "#044F67")
    lb6.place(relx = 0.05, rely = 0.80)
    en6 = Entry(LabelFrame)
    en6.place(relx = 0.3, rely = 0.80, relwidth = 0.62)

    #Submit Button
    SubmitBtn = Button(window, text = "SUBMIT", bg = '#264348', fg = 'white', command = gettingStuDetail)
    SubmitBtn.place(relx = 0.28, rely = 0.9, relwidth = 0.18, relheight= 0.08)

def Student():
    global headingframe1, headingframe2, Btn1, Btn2, headleble1, Canvas1
    headingframe1.destroy()
    headingframe2.destroy()
    Btn1.destroy()
    Btn2.destroy()
    Canvas1.destroy()
    headleble1.destroy()
    
    Canvas1 = Canvas(window)
    Canvas1.config(bg="#FFF9C4", width = imageSizeWidth, height = imageSizeHeight)
    Canvas1.pack(expand=True, fill=BOTH)

    headingframe1 = Frame(window, bg ="#333945", bd =5)
    headingframe1.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.13)

    headingframe2 = Frame(headingframe1, bg = "#EAF0F1")
    headingframe2.place(relx= 0.01, rely = 0.05, relwidth = 0.98, relheight = 0.9)

    headleble1 = Label(headingframe2, text = "Hello, Student", fg = 'black')
    headleble1.place(relx = 0.25, rely=0.15, relwidth = 0.5, relheight = 0.5)

    Btn1 = Button(window, text = "Register", bg = 'black', fg = 'white', command = StuRegister)
    Btn1.place(relx = 0.28, rely = 0.3, relwidth= 0.2, relheight = 0.1)

    Btn2 = Button(window, text = "Login", bg= 'black', fg = 'white', command = Login)
    Btn2.place(relx = 0.53, rely = 0.3, relwidth = 0.2, relheight = 0.1)

    Btn3 = Button(window, text = "Quit", bg = 'red', fg = 'white', command = window.quit)
    Btn3.place(relx = 0.53, rely = 0.9, relwidth = 0.18, relheight = 0.08)

#adding the background image
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

#top title of the LSM
headingframe1 = Frame(window, bg = "#333945", bd = 5)
headingframe1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingframe2 = Frame(headingframe1, bg = "#EAF0F1")
headingframe2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

headleble1 = Label(headingframe2, text="Welcome to LMS",fg = 'black')
headleble1.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.5)

#command means which function you wanna call from the button
# employee Button
Btn1 = Button(window, text = "Employee", bg = 'black', fg = 'white', command = Employee)
Btn1.place(relx = 0.25, rely = 0.3, relwidth = 0.2, relheight = 0.1)

# Student Button
Btn2 = Button(window, text = "Student", bg= 'black', fg = 'white', command = Student)
Btn2.place(relx = 0.55, rely = 0.3, relwidth = 0.2, relheight = 0.1)
window.mainloop()