
import cv2
import numpy as np
   
def fCanny(frame):
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    canny = cv2.Canny(img, 100, 200)
    canny = cv2.cvtColor(canny, cv2.COLOR_BGR2RGB)
    return canny
            
cap = cv2.VideoCapture('IFMA Campus Caxias.mp4')

while cap.isOpened():
    check, frame = cap.read()
    frame = cv2.resize(frame, (500, 400))
    if check == True:
        
        output = fCanny(frame)
        cv2.imshow("Canny", output)
        
        k = cv2.waitKey(20) & 0xFF
        if k == ord('q'):
            break
        
    else: break

cap.release()
cv2.destroyAllWindows()
