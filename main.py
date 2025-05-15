from functools import partial
from tkinter import *
from tkinter import ttk, messagebox
from turtle import width
import pymysql
import custom as cs
import credentials as cr
import validemail as vl

class Management:
    def __init__(self, root):
        self.window = root
        self.window.title("Contact Management System")
        self.window.geometry("940x480")
        self.window.config(bg = "white")

        #Customisation
        self.color_1 = cs.color_1
        self.color_2 = cs.color_2
        self.color_3 = cs.color_3
        self.color_4 = cs.color_4
        self.font_1 = cs.font_1
        self.font_2 = cs.font_2
        self.columns = cs.columns

        # User Credentials
        self.host = cr.host
        self.user = cr.user
        self.password = cr.password
        self.database = cr.database

        # Lest Frame
        self.frame_1 = Frame(self.window, bg = cs.color_1)
        self.frame_1.place(x=0, y=0, width=740, relheight=1)

        # Right Frame
        self.frame_2 = Frame(self.window, bg = cs.color_2)
        self.frame_2.place(x=740, y=0, relwidth=1, relheight=1)