
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

global countPeople
countPeople = 0

def deteccaoFaces(img):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(gray)# 1.3, 5

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            # uma pessoa tem face e boca 
            global countPeople
            countPeople = countPeople+1 
    
    return img
            
cap = cv2.VideoCapture('IFMA Campus Caxias - corte.mp4')

while cap.isOpened():
    check, frame = cap.read()
    frame = cv2.resize(frame, (800, 500))
    if check == True:
        
        output = deteccaoFaces(frame)
        cv2.imshow("Faces", output)
        
        k = cv2.waitKey(5) & 0xFF
        if k == ord('q'):
            print("O video tem '{}' pessoas".format(countPeople))
            break
        
    else: break

cap.release()
cv2.destroyAllWindows()
