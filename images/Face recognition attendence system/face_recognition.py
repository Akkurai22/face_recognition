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

class face_detector:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
       
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="Blue")
        title_lbl.place(x=0, y=0, width=1530, height=45) 

        # First image
        img1 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\face.jpg")   
        img1 = img1.resize((780, 700), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=50, width=780, height=700)

        # Second image
        img2 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\face_detector2.webp")   
        img2 = img2.resize((780, 700), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=780, y=50, width=780, height=700)

        b1_1 = Button(self.root, text="Face Detector", command=self.face_recog ,cursor="hand2", font=("times new roman", 12, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=1100, y=665, width=150, height=40)
    #-----------------------Attendence----------------
    def mark_attendence(self,i,r,n,d):
         with open ("akku.csv", "r+" ,newline="\n")as f:
              mydatalist =f.readlines()
              name_list=[]
              for line in mydatalist:
                   entry=line.split((","))
                   name_list.append(entry[0])
              if((i not in name_list) and (n not in name_list) and(d not in name_list) and (r not in name_list)):
                   now=datetime.now()
                   d1=now.strftime("%d/%m/%Y")
                   dtString=now.strftime("%H:%m:%S")
                   f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                   

              
              
              


    # ------------------- Face recognition -----------
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100 * (1 - predict / 300))
             
                conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select student_id from student where student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                my_cursor.execute("select Name from student where student_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Roll from student where student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select dep from student where student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                if confidence > 75:
                    cv2.putText(img, f"ID:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y-25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y+5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendence(i,r,n,d)

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord=[x,y,w,h]
            return coord

        def recognize(img, clf, faceCascade):
            img = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(2)

        if not video_cap.isOpened():
             print("Error: Could not open webcam.")
             messagebox.showerror("Error", "Could not open webcam. Please check the camera connection and permissions.")
             return

         # Set resolution (optional, can be adjusted)
        video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        while True:
              ret, img = video_cap.read()
              if not ret:
                        print("Error: Failed to capture image.")
                        break

              img = recognize(img, clf, faceCascade)
              cv2.imshow("Welcome to face recognition", img)

        # Break the loop when Enter key (13) is pressed
              if cv2.waitKey(1) == 13:
                break

    # Release the capture and close windows
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = face_detector(root)
    root.mainloop()
