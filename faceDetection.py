import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cas = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cas = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #1.3 decribes the accruracy of the model, 5 describes teh close proximity
    faces = face_cas.detectMultiScale(gray, 1.3, 5)

    #looping thourgh all teh faces
    for(x,y,w,h) in faces:
        #drawing the rectables for the faces
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255,0), 5)
        # comment - region of interest - roi
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        #now we have the face, we want to find the eyes only on teh face
        eyes = eye_cas.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 5)


    cv2.imshow('Image', frame)

    if(cv2.waitKey(1) == ord('q')):
        break


cap.release()
cv2.destroyAllWindows()