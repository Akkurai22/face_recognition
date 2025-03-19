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

class Help_desk:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="HELP DESK", font=("times new romen", 35, "bold"), bg="white", fg="Blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:images/help1.jpg")   
        img_top = img_top.resize((1530, 720), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        main_frame=Frame(f_lbl,bd=2)
        main_frame.place(x=500,y=600,width=600,height=80)

        dev_label1=Label(main_frame,text="Email:akankshrai22feb@gmail.com" ,font=("times new romen",25 ,"bold"),bg="white",fg="Blue")
        dev_label1.place(x=10,y=10)
        


if __name__ == "__main__":
    root = Tk()
    obj = Help_desk(root)
    root.mainloop()
