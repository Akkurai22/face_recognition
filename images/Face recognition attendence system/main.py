from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter
from student import Student
import os
from train import Train
from face_recognition import face_detector
from attendence import attendence
from developer import developer
from help import Help_desk
from exit import Exit
from time import strftime
from datetime import datetime


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First imagesss
        img1 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\img1.jpeg")   
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=500, height=130)

        # Second image
        img2 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\img3.jpeg")   
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=500, y=0, width=500, height=130)

        # Third image
        img3 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\img2.jpeg")   
        img3 = img3.resize((550, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=1000, y=0, width=550, height=130)

        # Background image
        img4 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\background1.jpg")   
        img4 = img4.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDENCE SYSTEM", font=("times new romen", 35, "bold"), bg="white", fg="Blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #----------------time------------
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl = Label(title_lbl, font=("times new romen", 15, "bold"), bg="white", fg="Blue")
        lbl.place(x=0, y=0, width=110, height=50)
        time()


       
        # Student button
        img5 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\student.webp")   
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        student_btn = Button(bg_img, image=self.photoimg5, command=self.student_details, cursor="hand2")
        student_btn.place(x=200, y=100, width=220, height=200)

        student_lbl = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new romen", 20, "bold"), bg="blue", fg="white")
        student_lbl.place(x=200, y=300, width=220, height=40)

        # Face detector button
        img6 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\img6.jpg")   
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        face_detector_btn = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.face_recognition)
        face_detector_btn.place(x=500, y=100, width=220, height=200)

        face_detector_lbl = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_recognition,font=("times new romen", 20, "bold"), bg="blue", fg="white")
        face_detector_lbl.place(x=500, y=300, width=220, height=40)

        # Attendance button
        img7 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\img7.jpg")   
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        attendance_btn = Button(bg_img, image=self.photoimg7,command=self.attendence_system, cursor="hand2")
        attendance_btn.place(x=800, y=100, width=220, height=200)

        attendance_lbl = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendence_system, font=("times new romen", 20, "bold"), bg="blue", fg="white")
        attendance_lbl.place(x=800, y=300, width=220, height=40)

        # Help Desk button
        img8 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\help.webp")   
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        help_desk_btn = Button(bg_img, image=self.photoimg8,command=self.help_desk, cursor="hand2")
        help_desk_btn.place(x=1100, y=100, width=220, height=200)

        help_desk_lbl = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help_desk, font=("times new romen", 20, "bold"), bg="blue", fg="white")
        help_desk_lbl.place(x=1100, y=300, width=220, height=40)

        # Train Data button
        img9 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\img9.webp")   
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        train_data_btn = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.train_data)
        train_data_btn.place(x=200, y=400, width=220, height=200)

        train_data_lbl = Button(bg_img, text="Train Data",cursor="hand2",command=self.train_data, font=("times new romen", 20, "bold"), bg="blue", fg="white")
        train_data_lbl.place(x=200, y=600, width=220, height=40)

        # Photos button
        img10 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\img4.jpg")   
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        photos_btn = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.open_img)
        photos_btn.place(x=500, y=400, width=220, height=200)
        
        photos_lbl = Button(bg_img, text="Photos",command=self.open_img, cursor="hand2", font=("times new romen", 20, "bold"), bg="blue", fg="white")
        photos_lbl.place(x=500, y=600, width=220, height=40)

        # Developer button
        img11 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\img10.webp")   
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        developer_btn = Button(bg_img, image=self.photoimg11,command=self.developer, cursor="hand2")
        developer_btn.place(x=800, y=400, width=220, height=200)

        developer_lbl = Button(bg_img, text="Developer", cursor="hand2",command=self.developer, font=("times new romen", 20, "bold"), bg="blue", fg="white")
        developer_lbl.place(x=800, y=600, width=220, height=40)

        # Exit button
        img12 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\exit1.jpg")   
        img12 = img12.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        exit_btn = Button(bg_img, image=self.photoimg12,command=self.iExit,  cursor="hand2")
        exit_btn.place(x=1100, y=400, width=220, height=200)
   
        exit_lbl = Button(bg_img, text="Exit",command=self.iExit,  cursor="hand2", font=("times new romen", 20, "bold"), bg="blue", fg="white")
        exit_lbl.place(x=1100, y=600, width=220, height=40)


  

    def open_img(self):
     os.startfile("data")

    def iExit(self):
        self.iExit= tkinter.messagebox.askyesno("face recognition","Are you sure exit this project")
        if self.iExit>0:
            self.root.destroy()
        else:
            return


    # Function to open Student Details window
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    
    def face_recognition(self):
        self.new_window = Toplevel(self.root)
        self.app = face_detector(self.new_window)


    def attendence_system(self):
        self.new_window = Toplevel(self.root)
        self.app = attendence(self.new_window)

    def help_desk(self):
        self.new_window = Toplevel(self.root)
        self.app = Help_desk(self.new_window)
    
    def developer(self):
        self.new_window = Toplevel(self.root)
        self.app = developer(self.new_window)
        
    def exit(self):
        self.new_window = Toplevel(self.root)
        self.app = Exit(self.new_window)
        
    
    


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
