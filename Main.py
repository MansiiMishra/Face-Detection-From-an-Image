#Importing OpenCV 
import cv2 
#Importing HARR CASCADE XML file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Uploading test image
img = cv2.imread('Test2.jpg')
#Converting to grey scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Allowing multiple face detection
faces = face_cascade.detectMultiScale(gray, 1.1, 6)
#Creating Rectangle around face
for(x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 250), 2)
#Displaying the image 
cv2.imshow('Detected Face Image',  img)
#Waiting for escape key for image to close
cv2.waitKey()
