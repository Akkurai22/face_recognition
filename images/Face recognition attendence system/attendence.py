from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import cv2
import numpy as np


class attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        # First image
        img1 = Image.open(r"images\img8.jpg")   
        img1 = img1.resize((800, 200), Image.Resampling.LANCZOS)  # Updated to LANCZOS
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=800, height=200)

        # Second image
        img2 = Image.open(r"images\img3.jpeg")   
        img2 = img2.resize((800, 200), Image.Resampling.LANCZOS)  # Updated to LANCZOS
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=800, y=0, width=800, height=200)

        #bg image
        img4 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\background1.jpg")   
        img4 = img4.resize((1530, 710), Image.Resampling.LANCZOS)  # Updated to LANCZOS
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img= Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl=Label(bg_img,text="ATTENDENCE SYSTEM", font=("times new romen",35 ,"bold"),bg="white",fg="Blue")
        title_lbl.place(x=0,y=0,width=1530,height=45) 

        main_frame=Frame(bg_img,bd=2 ,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

        #left label frame

        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendence system Details" , font=("times new romen",13 ,"bold"),bg="white",fg="Black")
        left_frame.place(x=10,y=10,width=730,height=580)

        img_left = Image.open(r"images\student.webp")   
        img_left = img_left.resize((730, 130), Image.Resampling.LANCZOS)  # Updated to LANCZOS
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl3 = Label(left_frame, image=self.photoimg_left)
        f_lbl3.place(x=5, y=0, width=720, height=130)

        left_inside_frame=Frame(main_frame,bd=2,bg="white",relief=RIDGE)


         #right label frame

        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details" , font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        right_frame.place(x=750,y=10,width=725,height=580)

        img_right = Image.open(r"images\student2.webp")   
        img_right= img_left.resize((730, 130), Image.Resampling.LANCZOS)  # Updated to LANCZOS
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl3 = Label(right_frame, image=self.photoimg_right)
        f_lbl3.place(x=5, y=1, width=720, height=130)


        



        










if __name__ == "__main__":
    root = Tk()
    obj = attendence(root)
    root.mainloop()
