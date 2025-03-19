from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import _mysql_connector
import os
import cv2
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="Blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top image
        img_top = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\face1.jpg")   
        img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)
        
        # Button for training
        b1_1 = Button(self.root, text="TRAIN DATA", cursor="hand2", command=self.train_classifier, font=("times new roman", 30, "bold"), bg="blue", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)

        # Bottom image
        img_bottom = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\train1.jpg")   
        img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
     data_dir = "data"
     path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) ]

     faces = []
     ids = []
     
     for image in path:
            img = Image.open(image).convert('L')  # Convert image to grayscale
            imageNp = np.array(img, 'uint8')
            
            # Safely extract the ID
           
            id = int(os.path.split[1].split('.')[1])  # Extract ID assuming consistent format
            
            faces.append(imageNp)
            ids.append(id)

            # Display the image while training (optional)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
     ids = np.array(ids)

     # Create and train the LBPH face recognizer
     clf = cv2.face.LBPHFaceRecognizer_create()  # Use the correct OpenCV method
     clf.train(faces, ids)
     clf.write("classifier.xml")  # Save the trained model
     cv2.destroyAllWindows()  # Close the OpenCV window

     messagebox.showinfo("Result", "Training datasets completed")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
