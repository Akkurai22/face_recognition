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
from main import Face_Recognition_System

def main():
 win=Tk()
 app=Login_Window(win)
 win.mainloop()

class LoginRegisterSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First Image
        img1 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\img1.jpeg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=500, height=130)

        # Second Image
        img2 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\img3.jpeg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=500, y=0, width=500, height=130)

        # Third Image
        img3 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\img2.jpeg")
        img3 = img3.resize((550, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=1000, y=0, width=550, height=130)

        # Background Image
        img4 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\background1.jpg")
        img4 = img4.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # Title
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM",
                          font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Time Display
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=("times new roman", 15, "bold"), bg="white", fg="blue")
        lbl.place(x=0, y=0, width=110, height=50)
        time()

        # Frames for Login and Registration
        self.login_frame = Frame(bg_img, bd=2, relief=RIDGE, bg="white")
        self.register_frame = Frame(bg_img, bd=2, relief=RIDGE, bg="white")
        self.setup_login_frame()

    # Database Connection
    def connect_to_database(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Test@123",
                database="face_recognizer"
            )
            return conn
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error connecting to database: {err}")
            exit()

    # Registration Functionality
    def register_user(self):
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()
        confirm_password = self.reg_confirm_password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required.")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        try:
            conn = self.connect_to_database()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration successful!")
            self.switch_to_login()
        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "Username already exists.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    # Login Functionality
    def login_user(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()

        try:
            conn = self.connect_to_database()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()
            conn.close()

            if user:
                messagebox.showinfo("Success", f"Welcome, {username}!")
                self.root.destroy()  # Close the login window
                os.system("python main.py")  # Open main.py
               
                # Add logic to open the main application here
            else:
                messagebox.showerror("Error", "Invalid username or password.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    # Setup Login Frame
    def setup_login_frame(self):
        self.login_frame.pack(pady=50)
        self.login_frame.place(x=550, y=200, width=400, height=350)

        Label(self.login_frame, text="Login", font=("Helvetica", 18, "bold"), bg="white").pack(pady=20)
        Label(self.login_frame, text="Username", bg="white").pack(pady=5)
        self.login_username_entry = Entry(self.login_frame, width=30)
        self.login_username_entry.pack(pady=5)

        Label(self.login_frame, text="Password", bg="white").pack(pady=5)
        self.login_password_entry = Entry(self.login_frame, show="*", width=30)
        self.login_password_entry.pack(pady=5)

        Button(self.login_frame, text="Login", command=self.login_user, width=15).pack(pady=20)
        Button(self.login_frame, text="Register", command=self.switch_to_register, width=15).pack()

    # Setup Register Frame
    def setup_register_frame(self):
        self.register_frame.pack()
        self.register_frame.place(x=550, y=200, width=400, height=400)

        Label(self.register_frame, text="Register", font=("Helvetica", 18, "bold"), bg="white").pack(pady=20)
        Label(self.register_frame, text="Username", bg="white").pack(pady=5)
        self.reg_username_entry = Entry(self.register_frame, width=30)
        self.reg_username_entry.pack(pady=5)

        Label(self.register_frame, text="Password", bg="white").pack(pady=5)
        self.reg_password_entry = Entry(self.register_frame, show="*", width=30)
        self.reg_password_entry.pack(pady=5)

        Label(self.register_frame, text="Confirm Password", bg="white").pack(pady=5)
        self.reg_confirm_password_entry = Entry(self.register_frame, show="*", width=30)
        self.reg_confirm_password_entry.pack(pady=5)

        Button(self.register_frame, text="Register", command=self.register_user, width=15).pack(pady=20)
        Button(self.register_frame, text="Back to Login", command=self.switch_to_login, width=15).pack()

    # Switch to Login Page
    def switch_to_login(self):
        self.register_frame.pack_forget()
        self.login_frame.pack()

    # Switch to Register Page
    def switch_to_register(self):
        self.login_frame.pack_forget()
        self.setup_register_frame()


if __name__ == "__main__":
    root = Tk()
    app = LoginRegisterSystem(root)
    root.mainloop()
