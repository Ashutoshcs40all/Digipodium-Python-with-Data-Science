import cv2

cap = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('face_detection.xml')
while True:

    # reading the frame
    ret, frame = cap.read()
    print(ret)
    # detecting the face
    print(frame)
    detected_faces = face_detector.detectMultiScale( frame, 1.1, 5)
  
    for (x,y,w,h) in detected_faces:
        cv2.rectangle(frame,(x,y),(x+w , y+h), (0,255,0),4)

    cv2.imshow('using webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()