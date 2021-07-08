
## library

import os
import cv2
from PIL import Image
import numpy as np
import cv2
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter.constants import S
import cv2
import numpy as np
from PIL import Image
import os

# Tkinter - for GUI

# Window - name given for GUI interface
window=tk.Tk()
# Title - Title for project
window.title("Face Recognition")
# resizable - make window fix shape
window.resizable(0,0)

# Label - for displaying text( l1 - is just id to identify)
l1=tk.Label(window,text="Name    ",font=("ALgerian",20))
# grid - to place the text in window (in row and column form)
l1.grid(column=0,row=0)
# Entry - give box for user to input
l1=tk.Entry(window,width=50)
l1.grid(column=1,row=0)


l2=tk.Label(window,text="id    ",font=("ALgerian",20))
l2.grid(column=0,row=1)
l2=tk.Entry(window,width=50)
l2.grid(column=1,row=1)

l3=tk.Label(window,text="Address    ",font=("ALgerian",20))
l3.grid(column=0,row=2)
l3=tk.Entry(window,width=50)
l3.grid(column=1,row=2)

l4=tk.Label(window,text="Phone    ",font=("ALgerian",20))
l4.grid(column=0,row=3)
l4=tk.Entry(window,width=50)
l4.grid(column=1,row=3)

##### This is the function used for detecting the face and storing in file
def trained_classifiers():
    # l1.get() - holds the input 
    if (l1.get()=="" or l2.get()=="" or l3.get()=="" or l4.get()==""):
        # display the message box 
        messagebox.showinfo("Please fill up the details")
    else:
        # code to connect to database
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="face_recognition"
        )
        mycursor=mydb.cursor()
        mycursor.execute("SELECT * from face")
        myresult=mycursor.fetchall()
        
        id=1
        for x in myresult:
            id +=1

        # send the datas to database
        sql="""insert into face(Name,id,Address,Phone) values(%s,%s,%s,%s)"""
        val=(l1.get(),id,l3.get(),l4.get())
        mycursor.execute(sql,val)
        mydb.commit()
        
        # hold the font face detection xml file
        trained_face_data=cv2.CascadeClassifier("C:\\Users\\Tech DD Twins\\Desktop\\Dipesh\\Face_recognition\\all\\sth.xml")
        
        # crop the image captured by webcam 
        def face_cropped(frame):
            #Convert image into gray image
            grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            # detect the face from gray image
            faces=trained_face_data.detectMultiScale(grayscaled_img,1.1,4)

            if faces is ():
                return None
            # get the coordinate and 
            for (x,y,w,h) in faces:
                cropped_face=frame[y:y+h,x:x+w]
                return cropped_face
                
        # allow webcam to capture image
        webcam=cv2.VideoCapture(0)
        name=l1.get()
        
        ids=0


        while True:
            # frame - store the captured image
            successful_frame,frame=webcam.read()
            if face_cropped(frame) is not None:
                ids+=1
                # resize the image and save in dir
                face=cv2.resize(face_cropped(frame),(200,200))
                
                grayscaled_img = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                # store image in given dir
                cv2.imwrite("C:\\Users\\Tech DD Twins\\Desktop\\Dipesh\\Face_recognition\\all\\photos\\"+f"{name}"+"."+f"{id}"+"."+f"{ids}"+".jpg",grayscaled_img)
                # Display the image
                cv2.imshow("Dipesh",grayscaled_img)
            if ids>25:
                break
            # 0 - allows us to move into another frame whereas -) 1 capture automatically
            cv2.waitKey(1)
            # Distroy all working windows
            cv2.destroyAllWindows()
            
        # Training the faces
        

        
        photos_dir="C:\\Users\\Tech DD Twins\\Desktop\\Dipesh\\Face_recognition\\all\\photos"
        #join the given path 
        path=[os.path.join(photos_dir,f) for f in os.listdir(photos_dir)]
        
        id1=[]
        ids=[]

        for image in path:
            # convert image into gray
            img = Image.open(image).convert("L")
            # IMage processing is done in array so converted into array
            imagenp=np.array(img)
            # Split image path
            id=int(os.path.split(image)[1].split(".")[1])
            # store in given id
            id1.append(imagenp)
            ids.append(id)
        #faces=np.array(faces)
        ids=np.array(ids)

        #Train and sava classifier

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(id1,ids)
        clf.write("C:\\Users\\Tech DD Twins\\Desktop\\Dipesh\\Face_recognition\\all\\classifers.xml")

        cv2.destroyAllWindows()

####
# Display the buttom where -) command perform action when clicked
b1=tk.Button(window,text="Register", font=("ALgerian",20),bg="white",command=trained_classifiers)

b1.grid(column=1,row=4)

# this function detect the object and display the name of person
def view():
    # Make the rectangle box over face
    def draw_boundry(img,classifier,scaleFactor,minNeighbours,color,text,clf):
        gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        trained=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)
        # pints where the actually the box is placed
        for (x,y,w,h) in trained:
            cv2.rectangle(img,(x,y),(x+w,y+h),color,2)

            id,pred=clf.predict(gray_image[y:y+h,x:x+w])
            # formula to find the confidence of image obtained
            confidence=int(100*(1-pred/300))

            # conecting to database
            mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="face_recognition"
            )
            mycursor=mydb.cursor()
            mycursor.execute("select name from face where id="+ str(id))
            s=mycursor.fetchone() # tuple

            #s=''+''.join(s)
            if type(s)==tuple: 
                s = ''+''.join(s) # string
            # store the name of person from database in s
            if confidence>85:
                cv2.putText(img,s,(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1,cv2.LINE_AA)
            # showing unknown person is obtained image is not in database
            else:
                cv2.putText(img,"Unknown",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),1,cv2.LINE_AA)
            
        return img

    trained_face_data=cv2.CascadeClassifier("C:\\Users\\Tech DD Twins\\Desktop\\Dipesh\\Face_recognition\\all\\sth.xml")
    clf=cv2.face.LBPHFaceRecognizer_create()
    clf.read("C:\\Users\\Tech DD Twins\\Desktop\\Dipesh\\Face_recognition\\all\\classifers.xml")
    webcam=cv2.VideoCapture(0)

    while True:
        successful_frame,img=webcam.read()
        img=draw_boundry(img,trained_face_data,1.3,6,(0,255,0),"Face",clf)
        cv2.imshow("hello",img)

        if cv2.waitKey(1)==13:
            break
    
    webcam.release()
    cv2.destroyAllWindows()

b2=tk.Button(window,text="Recognition", font=("ALgerian",20),bg="white",command=view)

b2.grid(column=1,row=6)

# Size of the GUI interface
window.geometry("800x400")
# make GUI to open when unless we press close symbol
window.mainloop()
