import random
import cv2
import numpy as np

def salt_pepper(img, prob):
    newImage = np.zeros(img.shape, np.uint8)
    chance = 1 - prob
    for i in range (img.shape[0]):
        for j in range (img.shape[1]):
            rand = random.random()
            if rand < prob:
                newImage[i][j] = 0
            elif rand > chance:
                newImage[i][j] = 255
            else:
                newImage[i][j] = img[i][j]
    return newImage
            
cap = cv2.VideoCapture('IFMA Campus Caxias.mp4')

prob = 0.05

while cap.isOpened():
    check, frame = cap.read()
    if check == True:
        
        k = cv2.waitKey(20) & 0xFF
                
        ruido = salt_pepper(frame, prob)
      
        cv2.imshow('Video Com Ruido', ruido)
        
        if k == ord('r') and prob < 1:
            print(prob)
            prob += 0.01
            
        if k == ord('p') and prob > 0:
            print(prob)
            prob -= 0.01
            
        if k == ord('q'):
            break
        
    else: break

cap.release()
cv2.destroyAllWindows()
