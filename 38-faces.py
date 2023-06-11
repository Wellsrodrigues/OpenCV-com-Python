import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
# mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_mcs_mouth.xml')
# mouth_cascade = cv2.CascadeClassifier('classificadores/haarcascade_mcs_mouth.xml')

img = cv2.imread('faces.jpg')
img = cv2.resize(img, (1080, 1020))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray)# 1.3, 5

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
    # mouth = mouth_cascade.detectMultiScale(roi_gray, 2.0, 20)
    # for (mx,my,mw,mh) in mouth:
    #     cv2.rectangle(roi_color,(mx,my),(mx+mw,my+mh),(0,0,255),2)
    
cv2.imshow('Deteccao',img)

cv2.waitKey(0)
cv2.destroyAllWindows()