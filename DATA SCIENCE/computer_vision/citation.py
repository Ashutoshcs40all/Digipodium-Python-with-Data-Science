import cv2 
import os

traineData =cv2.CascadeClassifier('face_detection.xml')

img = cv2.imread("faces.jpg")


graying = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faceCoordinates = traineData.detectMultiScale(graying)

for x,y,w,h in faceCoordinates:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)



cv2.imshow('window',img)
cv2.waitKey()



print("END OF PROGRAM")




