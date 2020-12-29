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


def issuebook():
    print("issue Book")