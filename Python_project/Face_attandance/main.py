from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os
from Student_1 import Student
from train import Train
from face_recognition import Face_recognition



class Face_Recognization_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x800+0+0")
        self.root.title("face Recognization System")

       
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
        

        #bg image
        
        # img_3=Image.open(r"C:\Users\Tech DD Twins\Desktop\Diwas\facedetection_attandence\photos\home_3.jpg")
        # img_33= img_3.resize((1530,700),Image.ANTIALIAS)
        # self.photoimg_3=ImageTk.PhotoImage(img_33)


        # bg_image=Label(self.root,image=self.photoimg_3)
        #bg_image.place(x=0,y=130,width=1530,height=900)

        
        # self.root.configure(bg="red")

        title_lbl= Label(root,text="Face Recognization Attendenance System Software",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1500,height=50)

        self.root.configure(bg="white")


        # student buttom
        but_1= Image.open(r"C:\Users\Tech DD Twins\Desktop\Diwas\facedetection_attandence\photos\but_1.jpg")
        but_1= but_1.resize((220,220),Image.ANTIALIAS)
        self.but_11= ImageTk.PhotoImage(but_1)

        b1=Button(root,image=self.but_11,command=self.Student_details,cursor="hand2")
        b1.place(x=150,y=150,width=220,height=150)

        b1_1=Button(root,text="Student Details",command=self.Student_details,bg="darkblue",cursor="hand2",font=("times new roman",12,"bold"),fg="white")
        b1_1.place(x=150,y=280,width=220,height=30)

        # Detect face button
        but_2= Image.open(r"C:\Users\Tech DD Twins\Desktop\Diwas\facedetection_attandence\photos\but_2.jpg")
        but_2= but_2.resize((220,220),Image.ANTIALIAS)
        self.but_22= ImageTk.PhotoImage(but_2)

        b2=Button(root,image=self.but_22,cursor="hand2",command=self.face_data)
        b2.place(x=450,y=150,width=220,height=150)

        b2_1=Button(root,bg="darkblue",text="Detect Face",cursor="hand2",command=self.face_data,font=("times new roman",12,"bold"),fg="white")
        b2_1.place(x=450,y=280,width=220,height=30)

        # Attendance
        but_3= Image.open(r"C:\Users\Tech DD Twins\Desktop\Diwas\facedetection_attandence\photos\but_3.jpg")
        but_3= but_3.resize((220,220),Image.ANTIALIAS)
        self.but_33= ImageTk.PhotoImage(but_3)

        b3=Button(root,image=self.but_33,cursor="hand2")
        b3.place(x=750,y=150,width=220,height=150)

        b3_1=Button(root,bg="darkblue",text="Attendance",cursor="hand2",font=("times new roman",12,"bold"),fg="white")
        b3_1.place(x=750,y=280,width=220,height=30)

        # Help
        but_4= Image.open(r"C:\Users\Tech DD Twins\Desktop\Diwas\facedetection_attandence\photos\but_4.jpg")
        but_4= but_4.resize((220,220),Image.ANTIALIAS)
        self.but_44= ImageTk.PhotoImage(but_4)

        b4=Button(root,image=self.but_44,cursor="hand2")
        b4.place(x=1050,y=150,width=220,height=150)

        b4_1=Button(root,bg="darkblue",text="Help",cursor="hand2",font=("times new roman",12,"bold"),fg="white")
        b4_1.place(x=1050,y=280,width=220,height=30)

        # Train data face
        but_5= Image.open(r"C:\Users\Tech DD Twins\Desktop\Diwas\facedetection_attandence\photos\but_5.jpg")
        but_5= but_5.resize((220,220),Image.ANTIALIAS)
        self.but_55= ImageTk.PhotoImage(but_5)

        b5=Button(root,image=self.but_11,cursor="hand2",command=self.train_data)
        b5.place(x=150,y=400,width=220,height=150)

        b5_1=Button(root,bg="darkblue",text="Train Face ",cursor="hand2",command=self.train_data,font=("times new roman",12,"bold"),fg="white")
        b5_1.place(x=150,y=530,width=220,height=30)

        # Photos face button
        but_6= Image.open(r"C:\Users\Tech DD Twins\Desktop\Diwas\facedetection_attandence\photos\but_6.jpg")
        but_6= but_6.resize((220,220),Image.ANTIALIAS)
        self.but_66= ImageTk.PhotoImage(but_6)

        b6=Button(root,image=self.but_66,cursor="hand2",command=self.open_img)
        b6.place(x=450,y=400,width=220,height=150)

        b6_1=Button(root,bg="darkblue",text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",12,"bold"),fg="white")
        b6_1.place(x=450,y=530,width=220,height=30)

        # Developer button
        but_7= Image.open(r"C:\Users\Tech DD Twins\Desktop\Diwas\facedetection_attandence\photos\but_7.jpg")
        but_7= but_7.resize((220,220),Image.ANTIALIAS)
        self.but_77= ImageTk.PhotoImage(but_7)

        b7=Button(root,image=self.but_77,cursor="hand2")
        b7.place(x=750,y=400,width=220,height=150)

        b7_1=Button(root,bg="darkblue",text="Developer",cursor="hand2",font=("times new roman",12,"bold"),fg="white")
        b7_1.place(x=750,y=530,width=220,height=30)

        # exit button
        but_8= Image.open(r"C:\Users\Tech DD Twins\Desktop\Diwas\facedetection_attandence\photos\but_8.jpg")
        but_8= but_8.resize((220,220),Image.ANTIALIAS)
        self.but_88= ImageTk.PhotoImage(but_8)

        b8=Button(root,image=self.but_88,cursor="hand2")
        b8.place(x=1050,y=400,width=220,height=150)

        b8_1=Button(root,bg="darkblue",text="Exit",cursor="hand2",font=("times new roman",12,"bold"),fg="white")
        b8_1.place(x=1050,y=530,width=220,height=30)


    def open_img(self):
        os.startfile("Data")
    
        #------------Function Buttons--------
    def Student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)
        


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognization_system(root)
    root.mainloop()




