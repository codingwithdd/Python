from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2
import os
import numpy as np
from numpy.lib.type_check import imag



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x800+0+0")
        self.root.title("face Recognization System")

        #title
        title_lbl= Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1535,height=50)

        #background color
        self.root.configure(bg="white")

        #top image
        img_top=Image.open(r"C:\Users\Tech DD Twins\Desktop\Diwas\facedetection_attandence\photos\home_3.jpg")
        img_22= img_top.resize((1532,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_22)


        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=5,y=50,width=1532,height=325)

        #button
        b1_1=Button(self.root,text="Train Data",command=self.train_classifier,bg="darkred",cursor="hand2",font=("times new roman",30,"bold"),fg="white")
        b1_1.place(x=0,y=400,width=1532,height=60)




    def train_classifier(self):
        data_dir=("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  # gray scale image
            image_np=np.array(img)
            id=int(os.path.split(image)[1].split(".")[1])

            faces.append(image_np)
            ids.append(id)
            cv2.imshow("Training",image_np)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #======= Train Classifier and save ======

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets Completed")


















if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()