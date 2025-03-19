from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import cv2
import numpy as np
import csv
from tkinter import filedialog



mydata=[]

class attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        #---------------variable---------

        self.var_attend_id=StringVar()
        self.var_roll_no=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendance=StringVar()

        





        # First image
        img1 = Image.open(r"images\img7.jpg")   
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
        left_inside_frame.place(x=5,y=170,width=720,height=300)


        #labeland entry

        #AttendanceID    
        attendanceId_label=Label(left_inside_frame, text="Attendance Id:",font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame ,width=20,textvariable=self.var_attend_id,font=("times new romen",12 ,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Name    
        Name_label=Label(left_inside_frame, text="Student Name:",font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        Name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_name,font=("times new romen",12 ,"bold"))
        Name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #Roll no  
        roll_no_label=Label(left_inside_frame, text="Roll no:",font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        roll_no_label .grid(row=1,column=0,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_roll_no,font=("times new romen",12 ,"bold"))
        roll_no_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #department 
        dep_label=Label(left_inside_frame, text="Department:",font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_dep,font=("times new romen",12 ,"bold"))
        dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #time    
        time_label=Label(left_inside_frame, text="Time:",font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_time,font=("comicsansns",12 ,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #Date  
        datelabel=Label(left_inside_frame, text="Date: :",font=("comicsansns",12 ,"bold"),bg="white",fg="Black")
        datelabel.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_date,font=("comicsansns",12 ,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        #Attendence   
        attendancelabel=Label(left_inside_frame, text="Attendance Status",font=("comicsansns",12 ,"bold"),bg="white",fg="Black")
        attendancelabel.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(left_inside_frame ,font=("comicsansns",12 ,"bold"),width=18,textvariable=self.var_attendance,state="readonly")
        gender_combo["value"]=("","status","Present","Absent")
        gender_combo.current(0)
        gender_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)
        
        import_csv_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new romen",12 ,"bold"),bg="blue",fg="white")
        import_csv_btn.grid(row=0,column=0)

        export_csv_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new romen",12 ,"bold"),bg="blue",fg="white")
        export_csv_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",width=17,font=("times new romen",12 ,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new romen",12 ,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
     
        

         #right label frame

        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details" , font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        right_frame.place(x=750,y=10,width=720,height=580)


        #table label frame

        table_frame=LabelFrame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=700,height=455)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll_no","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM , fill=X)
        scroll_y.pack(side=RIGHT , fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)



        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll_no",text="Roll no")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        
        self.AttendanceReportTable["show"]="headings"
    
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)


        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll_no",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        

        #fetch data

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    

    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV file","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv

    def exportCsv(self):
        try:
            if len(mydata) <1:
                messagebox.showerror("No Data","no data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("data Export","your data is exported to"+os.path.basename(fln)+"successfully")


        except Exception as es:
            # Show an error message if an exception occurs
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)




    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_roll_no.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attendance.set(rows[6])
  
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_roll_no.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = attendence(root)
    root.mainloop()
