from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #-------------------variable------------------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        # First image
        img1 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\img1.jpeg")   
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)  # Updated to LANCZOS
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=500, height=130)

        # Second image
        img2 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\img3.jpeg")   
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)  # Updated to LANCZOS
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=500, y=0, width=500, height=130)

        # Third image
        img3 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\img2.jpeg")   
        img3 = img3.resize((550, 130), Image.Resampling.LANCZOS)  # Updated to LANCZOS
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=1000, y=0, width=550, height=130)

       #bg image
        img4 = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\background1.jpg")   
        img4 = img4.resize((1530, 710), Image.Resampling.LANCZOS)  # Updated to LANCZOS
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img= Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl=Label(bg_img,text="Student Details", font=("times new romen",35 ,"bold"),bg="white",fg="Blue")
        title_lbl.place(x=0,y=0,width=1530,height=45) 

        main_frame=Frame(bg_img,bd=2 ,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)
        

        #left label frame

        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details" , font=("times new romen",13 ,"bold"),bg="white",fg="Black")
        left_frame.place(x=10,y=10,width=730,height=580)

        img_left = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\img2.jpeg")   
        img_left = img_left.resize((730, 130), Image.Resampling.LANCZOS)  # Updated to LANCZOS
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl3 = Label(left_frame, image=self.photoimg_left)
        f_lbl3.place(x=5, y=0, width=720, height=130)

        #current course
        current_cousre_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Cousre Infomation", font=("times new romen",12,"bold"),fg="Black")
        current_cousre_frame.place(x=5,y=135,width=720,height=150)

        #Department
        dep_label=Label(current_cousre_frame, text="Department",font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_cousre_frame ,textvariable=self.var_dep ,font=("times new romen",12 ,"bold"),state="readonly")
        dep_combo["value"]=("select department","computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #COURSE
        course_label=Label(current_cousre_frame, text="Course",font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_cousre_frame ,textvariable=self.var_course ,font=("times new romen",12 ,"bold"),state="readonly")
        dep_combo["value"]=("select Course","BCA","BBA","MCA","MBA")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #Year
        year_label=Label(current_cousre_frame, text="year",font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_cousre_frame ,textvariable=self.var_year ,font=("times new romen",12 ,"bold"),state="readonly")
        year_combo["value"]=("select year", "1st year", "2nd year")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_cousre_frame, text="Semester",font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_cousre_frame ,textvariable=self.var_semester ,font=("times new romen",12 ,"bold"),state="readonly")
        semester_combo["value"]=("select semester","semester-1","semester-2","semester-3","semester-4")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class Student Information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student infromation",font=("times new romen",12,"bold"),fg="Black")
        class_student_frame.place(x=5,y=260,width=720,height=300)
  
        #studentID    
        studentID_label=Label(class_student_frame, text="StudentID:",font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id ,width=20,font=("times new romen",12 ,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #studentName    
        studentName_label=Label(class_student_frame, text="Student Name:",font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name ,width=20,font=("times new romen",12 ,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #class division    
        class_div_label=Label(class_student_frame, text="Class Division:",font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        class_div_label .grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame ,textvariable=self.var_div,font=("times new romen",12 ,"bold"),width=18,state="readonly")
        div_combo["value"]=("","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        

        
        #Roll no 
        roll_no_label=Label(class_student_frame, text="Roll No:",font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new romen",12 ,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #Gender    
        gender_label=Label(class_student_frame, text="Gender:",font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame ,textvariable=self.var_gender,font=("times new romen",12 ,"bold"),width=18,state="readonly")
        gender_combo["value"]=("","Male","female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        

        #DateofBirth   
        dob_label=Label(class_student_frame, text="DOB :",font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new romen",12 ,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        #Email    
        email_label=Label(class_student_frame, text="Email:",font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        email_label .grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new romen",12 ,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #Phone no 
        phone_label=Label(class_student_frame, text="Phone No.:",font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new romen",12 ,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
  
        #address   
        address_label=Label(class_student_frame, text="Address:",font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        address_label .grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address ,width=20,font=("times new romen",12 ,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #Teacher Name
        teacher_label=Label(class_student_frame, text="Teacher Name:",font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher ,width=20,font=("times new romen",12 ,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio=StringVar()

        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio,text="Take Photo Sample",value="yes")
        radiobtn1.grid(row=5,column=0)

        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio,text="No Photo Sample",value="no")
        radiobtn2.grid(row=5,column=1)  

       #bbutton frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new romen",12 ,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new romen",12 ,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new romen",12 ,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new romen",12 ,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
     
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)


        take_photo_sample_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=35,font=("times new romen",12 ,"bold"),bg="blue",fg="white")
        take_photo_sample_btn.grid(row=0,column=0)

        upload_photo_sample_btn=Button(btn_frame1,text="Upload Photo Sample",width=35,font=("times new romen",12 ,"bold"),bg="blue",fg="white")
        upload_photo_sample_btn.grid(row=0,column=1)

        
        
        #right label frame

        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details" , font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        right_frame.place(x=750,y=10,width=725,height=580)

        img_right = Image.open(r"C:\Users\akank\OneDrive\Desktop\Face recognition attendence system\images\img12.jpg")   
        img_right= img_left.resize((730, 130), Image.Resampling.LANCZOS)  # Updated to LANCZOS
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl3 = Label(right_frame, image=self.photoimg_right)
        f_lbl3.place(x=5, y=1, width=720, height=130)



        #----------Serach system-------------
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search system",font=("times new romen",12,"bold"),fg="Black")
        search_frame.place(x=5,y=135,width=710,height=70)
          
        search_label=Label(search_frame, text="Search By:",font=("times new romen",12 ,"bold"),bg="white",fg="Black")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame ,font=("times new romen",12 ,"bold"),state="readonly")
        search_combo["value"]=("select","Roll no","Phone no",)
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new romen",12 ,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
       
        search_btn=Button(search_frame,text="Search",width=10,font=("times new romen",12 ,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=10,font=("times new romen",12 ,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)


        #----------------------table frame--------------------
        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM , fill=X)
        scroll_y.pack(side=RIGHT , fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="StudentName")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll_no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Dob")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSample")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)



        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        

        

       
        
        
    def add_data(self):
       if self.var_dep.get() == "select department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required")
       else:
        try:
            # Connect to the database
            conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="face_recognizer")
            my_cursor = conn.cursor()

            # SQL query to insert the data into the 'student' table
            my_cursor.execute("""
                INSERT INTO student (dep, course, year, semester, student_id, name, division, roll_no, gender, dob, email, phone_no, address, teacher, PhotoSample)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (
                                self.var_dep.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_semester.get(),
                                self.var_std_id.get(),
                                self.var_std_name.get(),
                                self.var_div.get(),
                                self.var_roll.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_email.get(),
                                self.var_phone.get(),
                                self.var_address.get(),
                                self.var_teacher.get(),
                                self.var_radio.get()
            ))

            # Commit the transaction and close the connection
            conn.commit()
            self.fetch_data()
            conn.close()

            # Show a success message
            messagebox.showinfo("Success", "Student details have been added successfully")

        except Exception as es:
            # Show an error message if an exception occurs
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    #---------------------fetch data--------------------------
    def fetch_data(self):
      try:
        # Establish connection to the database
        conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="face_recognizer")

        # Use the connection to create a cursor
        with conn.cursor() as my_cursor:
            # Execute SELECT query
            my_cursor.execute("SELECT * FROM student")
            data = my_cursor.fetchall()
            for row in data:
                       print(row)

            # If data is found, update the Treeview
            if data:
                self.student_table.delete(*self.student_table.get_children())  # Clear existing rows
                for row in data:
                    self.student_table.insert("", "end", values=row)  # Insert new rows
            else:
                pass
      except mysql.connector.Error as err:
        # Handle MySQL errors
            messagebox.showerror("Database Error", f"Error: {err}")
      except Exception as e:
        # Handle other errors
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
      finally:
        # Ensure the connection is closed
        if conn.is_connected():
            conn.close()

     

#-----------------get cursor------------------------
    def get_cursor(self, event=""):
      try:

        cursor_focus = self.student_table.selection()[0]

        # Retrieve the item data using the selection
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        # Set the values to the respective variables
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio.set(data[14])
    
      except IndexError:
        # Handle case when no row is selected
        messagebox.showerror("Error", "Please select a row to edit.")
      except Exception as e:
        # Handle unexpected errors
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

        
    #update function

    def update_data(self):
       if self.var_dep.get() == "select department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required",parent=self.root)

       else:
             try:
                   update=messagebox.askyesno("update","Do you want to update this student details",parent=self.root)
                   if update>0:
                         conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
                         my_cursor=conn.cursor() 
                         my_cursor.execute("update student set Dep=%s,course=%s,year=%s,semester=%s,name=%s,roll_no=%s,Division=%s,Gender=%s,Dob=%s,Email=%s,Phone_no=%s,Address=%s,teacher=%s,photoSample=%s where student_id=%s",(
                                                                self.var_dep.get(),
                                                                self.var_course.get(),
                                                                self.var_year.get(),
                                                                self.var_semester.get(),
                                                                self.var_std_name.get(),
                                                                self.var_div.get(),
                                                                self.var_roll.get(),
                                                                self.var_gender.get(),
                                                                self.var_dob.get(),
                                                                self.var_email.get(),
                                                                self.var_phone.get(),
                                                                self.var_address.get(),
                                                                self.var_teacher.get(),
                                                                self.var_radio.get(),
                                                                self.var_std_id.get()             


                         ))
            
                   else:
                       if  not update:
                             return
                   messagebox.showinfo("success","Student detail successfully update competed",parent=self.root)
                   conn.commit()
                   self.fetch_data()
                   conn.close()
             except Exception as es:
                   messagebox.showerror("Error",f"Due to :{str(es)},parent=self.root")



#------------delete function---------------------

    def delete_data(self):
      if self.var_std_id.get=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
      else:
            try:
                  delete=messagebox.askyesno("student delete page","do you want to delete this student",parent=self.root)
                  if delete>0:
                       conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
                       my_cursor=conn.cursor() 
                       sql="delete from student where student_id=%s"
                       val=(self.var_std_id.get(),)
                       my_cursor.execute(sql,val)
                  else:
                       if not delete:
                            return
                       
                  conn.commit()
                  self.fetch_data()
                  conn.close()
                  messagebox.showinfo("delete","successfully deleted!!!")
            except Exception as es:
                   messagebox.showerror("Error",f"Due to :{str(es)},parent=self.root")

    #-------------------reset function------------------

    def reset_data(self):
          self.var_dep.set("Select Department")
          self.var_course.set("select Course")
          self.var_year.set("select year")
          self.var_semester.set("Select Semester")
          self.var_std_name.set("")
          self.var_std_id.set("")
          self.var_div.set("")
          self.var_roll.set("")
          self.var_gender.set("")
          self.var_dob.set("")
          self.var_email.set("")
          self.var_phone.set("")
          self.var_address.set("")
          self.var_teacher.set("")
          self.var_radio.set("")

  #-----------------------generate  data set or Take sample phot0
             
    def generate_dataset(self):
     if self.var_dep.get() == "select department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
     else:
        try:
            # Database connection
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Test@123", database="face_recognizer"
            )
            my_cursor = conn.cursor()
            
            # Update student details
            my_cursor.execute(
                """
                UPDATE student SET Dep=%s, course=%s, year=%s, semester=%s, name=%s, roll_no=%s, 
                Division=%s, Gender=%s, Dob=%s, Email=%s, Phone_no=%s, Address=%s, teacher=%s, 
                photoSample=%s WHERE student_id=%s
                """,
                (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_roll.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    "Yes",
                    self.var_std_id.get(),  # Pass the correct student ID
                ),
            )
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()

            # Load predefined data for face detection
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                """Detect and crop faces from the frame."""
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    face = img[y:y + h, x:x + w]
                    return face
                return None

            # Open webcam to capture face images
            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, my_frame = cap.read()
                if not ret:
                    break

                cropped_face = face_cropped(my_frame)
                if cropped_face is not None:
                    img_id += 1
                    face = cv2.resize(cropped_face, (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)

                # Stop when Enter key is pressed or 100 images are captured
                if cv2.waitKey(1) == 13 or img_id == 100:
                    break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Generating Data sets completed!!!", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    
            



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
