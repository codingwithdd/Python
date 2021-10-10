from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2

import numpy as np
from numpy.lib.type_check import imag





class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x800+0+0")
        self.root.title("face Recognization System")

        #title
        title_lbl= Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="brown")
        title_lbl.place(x=0,y=0,width=1535,height=50)

        #background color
        self.root.configure(bg="white")

        #top image
        img_top=Image.open(r"C:\Users\Tech DD Twins\Desktop\Diwas\facedetection_attandence\photos\home_3.jpg")
        img_top= img_top.resize((1532,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)


        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=5,y=50,width=1532,height=325)

        #button
        b1_1=Button(self.root,text="Detect",command=self.face_recog,bg="red",cursor="hand2",font=("times new roman",30,"bold"),fg="white")
        b1_1.place(x=0,y=400,width=1532,height=60)

        #======== face recognition  ======

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                cnx=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="database_1")
                cursor=cnx.cursor()

                cursor.execute("select Name from student where Student_id="+str(id))
                n=str(cursor.fetchone())
                print(n)
                n="+".join(n)

                cursor.execute("select Roll from student where Student_id="+str(id))
                r=str(cursor.fetchone())
                r="+".join(r)

                cursor.execute("select Dep from student where Student_id="+str(id))
                d=str(cursor.fetchone())
                d="+".join(d)




                if confidence>75:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        
        while True:
            
            ret,img=video_cap.read()
            img1=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img1)
            """
            if cv2.waitKey(1)==13:
                break
            """
            key= cv2.waitKey(1)
            if key==ord("q"):
                break
            

        video_cap.release()
        cv2.destroyAllWindows()



if __name__=="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()