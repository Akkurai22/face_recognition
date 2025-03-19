from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import cv2
import numpy as np
from time import strftime
from datetime import datetime

class developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new romen", 35, "bold"), bg="white", fg="Blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"images/img4.jpg")   
        img_top = img_top.resize((1530, 720), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=100,y=50,width=500,height=600)

        img1=Image.open("images/deepika.webp")  
        img1 = img_top.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(main_frame, image=self.photoimg1)
        f_lbl.place(x=150, y=20, width=200, height=200)

        dev_label1=Label(main_frame,text="Hello I am Deepika Padukone" ,font=("times new romen",12 ,"bold"),bg="white",fg="Blue")
        dev_label1.place(x=120,y=230)

        dev_label2=Label(main_frame,text="I am Full Stack Developer" ,font=("times new romen",12 ,"bold"),bg="white",fg="Blue")
        dev_label2.place(x=120,y=250)

        img2 = Image.open("images/img8.jpg")
        img2= img_top.resize((500, 600), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=0, y=270, width=500, height=600)




if __name__ == "__main__":
    root = Tk()
    obj = developer(root)
    root.mainloop()
