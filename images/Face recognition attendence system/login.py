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



class login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

    
       

# Database Connection
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",  # Replace with your MySQL host
            user="root",       # Replace with your MySQL username
            password="Test@123",  # Replace with your MySQL password
            database="face_recognizer"  # Replace with your database name
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error connecting to database: {err}")
        exit()


# Registration Functionality
def register_user():
    username = reg_username_entry.get()
    password = reg_password_entry.get()
    confirm_password = reg_confirm_password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "All fields are required.")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return

    try:
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Registration successful!")
        switch_to_login()
    except mysql.connector.IntegrityError:
        messagebox.showerror("Error", "Username already exists.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Login Functionality
def login_user():
    username = login_username_entry.get()
    password = login_password_entry.get()

    try:
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            messagebox.showinfo("Success", f"Welcome, {username}!")
            root.destroy()
            # Add logic to open the main application here
        else:
            messagebox.showerror("Error", "Invalid username or password.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Switch to Login Page
def switch_to_login():
    reg_frame.pack_forget()
    login_frame.pack()


# Switch to Register Page
def switch_to_register():
    login_frame.pack_forget()
    reg_frame.pack()


# Main Application Window
root = Tk()
root.title("Login and Registration System")
root.geometry("1530x790")

# Login Frame
login_frame = Frame(root)
login_frame.pack()

Label(login_frame, text="Login", font=("Helvetica", 18, "bold")).pack(pady=10)
Label(login_frame, text="Username").pack()
login_username_entry = Entry(login_frame)
login_username_entry.pack(pady=5)

Label(login_frame, text="Password").pack()
login_password_entry = Entry(login_frame, show="*")
login_password_entry.pack(padx=100,pady=5)

Button(login_frame, text="Login", command=login_user).pack(pady=10)
Button(login_frame, text="Register", command=switch_to_register).pack()

# Registration Frame
reg_frame = Frame(root)

Label(reg_frame, text="Register", font=("Helvetica", 18, "bold")).pack(pady=10)
Label(reg_frame, text="Username").pack()
reg_username_entry = Entry(reg_frame)
reg_username_entry.pack(pady=5)

Label(reg_frame, text="Password").pack()
reg_password_entry = Entry(reg_frame, show="*")
reg_password_entry.pack(pady=5)

Label(reg_frame, text="Confirm Password").pack()
reg_confirm_password_entry = Entry(reg_frame, show="*")
reg_confirm_password_entry.pack(pady=5)

Button(reg_frame, text="Register", command=register_user).pack(pady=10)
Button(reg_frame, text="Back to Login", command=switch_to_login).pack()

# Start with Login Frame
switch_to_login()

if __name__ == "__main__":
    root = Tk()
    obj = login(root)
    root.mainloop()
