import cv2
from random import randrange

# load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data=cv2.CascadeClassifier("sth.xml")

# Choose an image to detect the faces
# img=cv2.imread("index.jpeg")

# Detect the webcam if we put zero else give video file name
webcam=cv2.VideoCapture(0)


while True:
    #Read the current frame
    successful_frame,frame=webcam.read()

    # Convert to graystyle
    grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # find the coordinate of rectangle along with height and width
    (x,y,w,h)=face_coordinates[0]

    # Draw rectangle around the faces
    cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(156,256),randrange(256),randrange(256)),2)

    #Display the image with the faces
    cv2.imshow("Dipesh",frame)
    key=cv2.waitKey(1)

    #stop id "q" is pressed
    if key==81 or key==13:
        break
#release the videocapture object
webcam.release()

"""
# Convert to graystyle
grayscaled_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# print(face_coordinates)

# find the coordinate of rectangle along with height and width
(x,y,w,h)=face_coordinates[0]

# Draw rectangle around the faces
cv2.rectangle(img,(x,y),(x+w,y+w),(randrange(156,256),randrange(256),randrange(256)),2)

#Display the image with the faces
cv2.imshow("Dipesh",img)



# 
cv2.waitKey()
"""
# 


print("code completed")
