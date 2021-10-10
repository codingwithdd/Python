from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2
import os



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x800+0+0")
        self.root.title("face Recognization System")

        #==========variable========
        self.var_Dep=StringVar()
        self.var_Course=StringVar()
        self.var_Year=StringVar()
        self.var_Semester=StringVar()
        self.var_Student_id=StringVar()
        self.var_Name=StringVar()
        self.var_Div=StringVar()
        self.var_Roll=StringVar()
        self.var_Gender=StringVar()
        self.var_Dob=StringVar()
        self.var_Email=StringVar()
        self.var_Phone=StringVar()
        self.var_Address=StringVar()
        self.var_Guardian=StringVar()
        self.var_PhotoSample=StringVar()

        #First image
        img=Image.open(r"C:\Users\Tech DD Twins\Desktop\Diwas\facedetection_attandence\photos\home_6.jpg")
        img= img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)


        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        #second image
        img_1=Image.open(r"C:\Users\Tech DD Twins\Desktop\Diwas\facedetection_attandence\photos\home_5.jpg")
        img_11= img_1.resize((500,130),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_11)


        f_lbl=Label(self.root,image=self.photoimg_1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third image
        img_2=Image.open(r"C:\Users\Tech DD Twins\Desktop\Diwas\facedetection_attandence\photos\home_3.jpg")
        img_22= img_2.resize((500,130),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_22)


        f_lbl=Label(self.root,image=self.photoimg_2)
        f_lbl.place(x=1000,y=0,width=600,height=130)

        #title
        title_lbl= Label(root,text="Student Management Software",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1535,height=50)


        #background color
        self.root.configure(bg="black")

        #main frame
        main_frame=Frame(root,bd=2)
        main_frame.place(x=10,y=140,width=1515,height=645)


        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Enter Student Details",font=("times new roman",14,"bold"))
        Left_frame.place(x=10,y=10,width=770,height=620)

        #image in left frame
        left_img=Image.open(r"C:\Users\Tech DD Twins\Desktop\Diwas\facedetection_attandence\photos\home_6.jpg")
        left_img.resize((750,80),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(left_img)

        left_lbl=Label(Left_frame,image=self.photoimg_left)
        left_lbl.place(x=5,y=0,width=750,height=80)

        # current course
        Current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Course Information",font=("times new roman",14,"bold"))
        Current_course_frame.place(x=5,y=85,width=750,height=120)

        #Department
        dep_label=Label(Current_course_frame,text="Department",font=("times new roman",15,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_Dep,font=("times new roman",13,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Science","Management","Law","Humanities")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #course
        course_label=Label(Current_course_frame,text="Course",font=("times new roman",15,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_Course,font=("times new roman",13,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","NEB","A label","Other")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(Current_course_frame,text="Year",font=("times new roman",15,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_Year,font=("times new roman",13,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2078","2079","2080","2081","2082","2083","2084","2085","2086","2087","2088","2089","2090")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(Current_course_frame,text="Semester",font=("times new roman",15,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_Semester,font=("times new roman",13,"bold"),width=17,state="readonly")
        semester_combo["values"]=("Select Semester","First","Second","Third","Forth","Fifth","Sixth","Seventh","Eighth")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        # Class Student information
        Class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",14,"bold"))
        Class_student_frame.place(x=5,y=215,width=750,height=215)

        #Student ImageID
        StudentId_label=Label(Class_student_frame,text="Student ID :",font=("times new roman",13,"bold"),bg="white")
        StudentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        StudentId_entry=ttk.Entry(Class_student_frame,textvariable=self.var_Student_id,width=20,font=("times new roman",13,"bold"))
        StudentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #Student name 
        Student_name_label=Label(Class_student_frame,text="Student Name :",font=("times new roman",13,"bold"),bg="white")
        Student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Student_name_entry=ttk.Entry(Class_student_frame,textvariable=self.var_Name,width=20,font=("times new roman",13,"bold"))
        Student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Class division 
        Class_div_label=Label(Class_student_frame,text="Class Division :",font=("times new roman",13,"bold"),bg="white")
        Class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        # Class_div_entry=ttk.Entry(Class_student_frame,width=20,font=("times new roman",13,"bold"))
        # Class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        Class_div_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_Div,font=("times new roman",13,"bold"),width=18,state="readonly")
        Class_div_combo["values"]=("Select Division","A","B","C","D","E","F","G")
        Class_div_combo.current(0)
        Class_div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll No 
        Roll_no_label=Label(Class_student_frame,text="Roll No :",font=("times new roman",13,"bold"),bg="white")
        Roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Roll_no_entry=ttk.Entry(Class_student_frame,textvariable=self.var_Roll,width=20,font=("times new roman",13,"bold"))
        Roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender 
        Gender_label=Label(Class_student_frame,text="Gender :",font=("times new roman",13,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        # Gender_entry=ttk.Entry(Class_student_frame,width=20,font=("times new roman",13,"bold"))
        # Gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        Gender_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_Gender,font=("times new roman",13,"bold"),width=18,state="readonly")
        Gender_combo["values"]=("Select Gender","Male","Female","Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Date of birth
        Dob_label=Label(Class_student_frame,text="DOB :",font=("times new roman",13,"bold"),bg="white")
        Dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Dob_entry=ttk.Entry(Class_student_frame,textvariable=self.var_Dob,width=20,font=("times new roman",13,"bold"))
        Dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email 
        Email_label=Label(Class_student_frame,text="Email :",font=("times new roman",13,"bold"),bg="white")
        Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Email_entry=ttk.Entry(Class_student_frame,textvariable=self.var_Email,width=20,font=("times new roman",13,"bold"))
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone 
        Phone_label=Label(Class_student_frame,text="Phone No :",font=("times new roman",13,"bold"),bg="white")
        Phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        Phone_entry=ttk.Entry(Class_student_frame,textvariable=self.var_Phone,width=20,font=("times new roman",13,"bold"))
        Phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        Address_label=Label(Class_student_frame,text="Address :",font=("times new roman",13,"bold"),bg="white")
        Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Address_entry=ttk.Entry(Class_student_frame,textvariable=self.var_Address,width=20,font=("times new roman",13,"bold"))
        Address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Guardian name
        Guardian_label=Label(Class_student_frame,text="Guardian Name :",font=("times new roman",13,"bold"),bg="white")
        Guardian_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        Guardian_entry=ttk.Entry(Class_student_frame,textvariable=self.var_Guardian,width=20,font=("times new roman",13,"bold"))
        Guardian_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        # Action Button
        Action_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Action Button",font=("times new roman",14,"bold"))
        Action_frame.place(x=5,y=430,width=750,height=160)

        #radio buttons
        self.var_PhotoSample=StringVar()
        radio_b1=ttk.Radiobutton(Action_frame,variable=self.var_PhotoSample, text="Take a Photo Sample", value="Yes")
        radio_b1.grid(row=0,column=0,padx=50,pady=5,sticky=W)

        radio_b2=ttk.Radiobutton(Action_frame,variable=self.var_PhotoSample,text="No Photo Sample", value="No")
        radio_b2.grid(row=0,column=1,padx=50,pady=5,sticky=W)

        # button frame
        btn_frame=Frame(Action_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=40,width=725,height=40)

        #save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        #update button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        #delete button
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        #reset button
        reset_button=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        reset_button.grid(row=0,column=3)


        #second  button frame
        btn_frame1=Frame(Action_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=10,y=90,width=725,height=40)

        #take photo button
        
        take_photo_button=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=30,font=("times new roman",15,"bold"),bg="blue",fg="white")
        take_photo_button.grid(row=0,column=0)

        #update photo
        update_photo_button=Button(btn_frame1,text="Update Photo Sample",width=30,font=("times new roman",15,"bold"),bg="blue",fg="white")
        update_photo_button.grid(row=0,column=1)
        



        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Find Student Details",font=("times new roman",14,"bold"))
        Right_frame.place(x=800,y=10,width=700,height=620)

        #image in right frame
        right_img=Image.open(r"C:\Users\Tech DD Twins\Desktop\Diwas\facedetection_attandence\photos\home_6.jpg")
        right_img.resize((750,80),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(right_img)

        right_lbl=Label(Right_frame,image=self.photoimg_right)
        right_lbl.place(x=5,y=0,width=680,height=80)


        #--------Search System----------

        #search details frame
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search Details",font=("times new roman",14,"bold"))
        Search_frame.place(x=5,y=85,width=685,height=80)

        #search bar
        Search_label=Label(Search_frame,text="Search By :",font=("times new roman",13,"bold"),bg="gray",fg="white")
        Search_label.grid(row=0,column=0,padx=2,pady=5,sticky=W)

        Search_combo=ttk.Combobox(Search_frame,font=("times new roman",13,"bold"),width=14,state="readonly")
        Search_combo["values"]=("Select","Student Name","Roll No","Phone Number","Address")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #search entry
        Search_entry=ttk.Entry(Search_frame,width=14,font=("times new roman",13))
        Search_entry.grid(row=0,column=2,padx=2,pady=5,sticky=W)

        #Search Button
        Search_btn=Button(Search_frame,text="Search",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=2)

        # Show all button
        Show_all_button=Button(Search_frame,text="Show All",width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Show_all_button.grid(row=0,column=4)


        #-------table frame -------
        Table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=5,y=170,width=685,height=420)

        #Scroll Bae
        Scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        
        self.Student_table=ttk.Treeview(Table_frame,column=("Dep","Course","Year","Sem","ID","Name","Div","Roll","Gender","Dob","Email","Phone","Address","Guardian","Photo"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x.config(command=self.Student_table.xview)
        Scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("Dep",text="Department")
        self.Student_table.heading("Course",text="Course")
        self.Student_table.heading("Year",text="Year")
        self.Student_table.heading("Sem",text="Semester")
        self.Student_table.heading("ID",text="StudentID")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("Div",text="Division")
        self.Student_table.heading("Roll",text="Roll")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("Dob",text="DOB")
        self.Student_table.heading("Email",text="Email")
        self.Student_table.heading("Phone",text="Phone")
        self.Student_table.heading("Address",text="Address")
        self.Student_table.heading("Guardian",text="Guardian")
        self.Student_table.heading("Photo",text="PhotoSampleStatus")
        self.Student_table["show"]="headings"

        self.Student_table.column("Dep",width=100)
        self.Student_table.column("Course",width=100)
        self.Student_table.column("Year",width=100)
        self.Student_table.column("Sem",width=100)
        self.Student_table.column("ID",width=100)
        self.Student_table.column("Name",width=100)
        self.Student_table.column("Div",width=100)
        self.Student_table.column("Roll",width=100)
        self.Student_table.column("Gender",width=100)
        self.Student_table.column("Dob",width=100)
        self.Student_table.column("Email",width=100)
        self.Student_table.column("Phone",width=100)
        self.Student_table.column("Address",width=100)
        self.Student_table.column("Guardian",width=100)
        self.Student_table.column("Photo",width=100)

    

        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #-----------------Fuction Deceleration
    
    def add_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_Student_id.get()=="" or self.var_Semester.get()=="Select Semester" or self.var_Div.get()=="Select Division" or self.var_Year.get()=="Select Year"or self.var_Course.get()=="Select Course" or self.var_Roll.get()=="" or self.var_Gender.get()=="Select Gender" or self.var_Dob.get()=="" or self.var_Email.get()=="" or self.var_Address.get()=="" or self.var_Guardian.get()=="" or self.var_PhotoSample.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            
            cnx=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="database_1")
            cursor=cnx.cursor()
            try:
                cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                            
                                                                                            self.var_Dep.get(),
                                                                                            self.var_Course.get(),
                                                                                            self.var_Year.get(),
                                                                                            self.var_Semester.get(),
                                                                                            self.var_Student_id.get(),
                                                                                            self.var_Name.get(),
                                                                                            self.var_Div.get(),
                                                                                            self.var_Roll.get(),
                                                                                            self.var_Gender.get(),
                                                                                            self.var_Dob.get(),
                                                                                            self.var_Email.get(),
                                                                                            self.var_Phone.get(),
                                                                                            self.var_Address.get(),
                                                                                            self.var_Guardian.get(),
                                                                                            self.var_PhotoSample.get()))
                
                cnx.commit()
                self.fetch_data()
                cnx.close()
                messagebox.showinfo("Success","Students details has been added Successfully",parent=self.root)
                    
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)




     #=============Fetch Data===============
    def fetch_data(self):
        cnx=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="database_1")
        cursor=cnx.cursor()
        cursor.execute("Select * from student")
        data=cursor.fetchall()

        if len(data)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for i in data:
                self.Student_table.insert("",END,values=i)
            cnx.commit()
        cnx.close()


    #===== get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.Student_table.focus()
        content=self.Student_table.item(cursor_focus)
        data=content["values"]

        self.var_Dep.set(data[0])
        self.var_Course.set(data[1])
        self.var_Year.set(data[2])
        self.var_Semester.set(data[3])
        self.var_Student_id.set(data[4])
        self.var_Name.set(data[5])
        self.var_Div.set(data[6])
        self.var_Roll.set(data[7])
        self.var_Gender.set(data[8])
        self.var_Dob.set(data[9])
        self.var_Email.set(data[10])
        self.var_Phone.set(data[11])
        self.var_Address.set(data[12])
        self.var_Guardian.set(data[13])
        self.var_PhotoSample.set(data[14])



    #=== update function
    def update_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_Student_id.get()=="" or self.var_Semester.get()=="Select Semester" or self.var_Div.get()=="Select Division" or self.var_Year.get()=="Select Year"or self.var_Course.get()=="Select Course" or self.var_Roll.get()=="" or self.var_Gender.get()=="Select Gender" or self.var_Dob.get()=="" or self.var_Email.get()=="" or self.var_Address.get()=="" or self.var_Guardian.get()=="" or self.var_PhotoSample.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)

        else:
            try:
                update1=messagebox.askyesno("Update","Do you want to upgrade this student details",parent=self.root)
                if update1>0:
                    cnx=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="database_1")
                    cursor=cnx.cursor()
                    cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Guardian=%s,PhotoSample=%s where Student_id=%s",(

                                                                                            self.var_Dep.get(),
                                                                                            self.var_Course.get(),
                                                                                            self.var_Year.get(),
                                                                                            self.var_Semester.get(),
                                                                                            self.var_Name.get(),
                                                                                            self.var_Div.get(),
                                                                                            self.var_Roll.get(),
                                                                                            self.var_Gender.get(),
                                                                                            self.var_Dob.get(),
                                                                                            self.var_Email.get(),
                                                                                            self.var_Phone.get(),
                                                                                            self.var_Address.get(),
                                                                                            self.var_Guardian.get(),
                                                                                            self.var_PhotoSample.get(),
                                                                                            self.var_Student_id.get()))

                else:
                    if not update1:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                cnx.commit()
                self.fetch_data()
                cnx.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #  delete function
    def delete_data(self):
        if self.var_Student_id.get()=="":
            messagebox.showerror("Error","Student id must be selected",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    cnx=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="database_1")
                    cursor=cnx.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_Student_id.get(),)
                    cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                cnx.commit()
                self.fetch_data()
                cnx.close()
                messagebox.showinfo("Delete","Successsfully deleted student details",parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent= self.root)


    # reset function
    def reset_data(self):
        self.var_Dep.set("Select Department")
        self.var_Course.set("Select Course")
        self.var_Year.set("Select Year")
        self.var_Semester.set("Select Semester")
        self.var_Student_id.set("")
        self.var_Name.set("")
        self.var_Div.set("Select Division")
        self.var_Roll.set("")
        self.var_Gender.set("Select Gender")
        self.var_Dob.set("")
        self.var_Email.set("")
        self.var_Phone.set("")
        self.var_Address.set("")
        self.var_Guardian.set("")
        self.var_PhotoSample.set("")



    #========== Generate Data set or take photo sample
    def generate_dataset(self):
        if self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_Student_id.get()=="" or self.var_Semester.get()=="Select Semester" or self.var_Div.get()=="Select Division" or self.var_Year.get()=="Select Year"or self.var_Course.get()=="Select Course" or self.var_Roll.get()=="" or self.var_Gender.get()=="Select Gender" or self.var_Dob.get()=="" or self.var_Email.get()=="" or self.var_Address.get()=="" or self.var_Guardian.get()=="" or self.var_PhotoSample.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)

        else:
            try:
                cnx=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="database_1")
                cursor=cnx.cursor()
                cursor.execute("Select * from student")
                myresult=cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Guardian=%s,PhotoSample=%s where Student_id=%s",(

                                                                                            self.var_Dep.get(),
                                                                                            self.var_Course.get(),
                                                                                            self.var_Year.get(),
                                                                                            self.var_Semester.get(),
                                                                                            self.var_Name.get(),
                                                                                            self.var_Div.get(),
                                                                                            self.var_Roll.get(),
                                                                                            self.var_Gender.get(),
                                                                                            self.var_Dob.get(),
                                                                                            self.var_Email.get(),
                                                                                            self.var_Phone.get(),
                                                                                            self.var_Address.get(),
                                                                                            self.var_Guardian.get(),
                                                                                            self.var_PhotoSample.get(),
                                                                                            self.var_Student_id.get()==id+1))

                cnx.commit()
                self.fetch_data()
                self.reset_data()
                cnx.close()
            

                #===== load predifined dataa on face frontals from opencv

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum Neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_cropped(myframe) is  not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="Data/user."+str(id) + "."+ str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Sets completed!!!")

            except EXCEPTION as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent= self.root)










        




                    












    














if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
