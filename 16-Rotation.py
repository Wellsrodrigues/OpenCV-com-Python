import cv2
import numpy as np


img = cv2.imread("ifma-caxias.jpg")

(rows, cols) = img.shape[0:2]

point = []

def click(event,x,y,flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,0,255),-1)
        point.append(x)
        point.append(y)
        
# def rotateImg(rot):
#     M = cv2.getRotationMatrix2D(point, rot, 1)
#     out = cv2.warpAffine(img, M, (cols, rows))
#     return out

def rotateImg(rot):
    out = np.zeros(img.shape, np.uint8)
    for i in range (rows):
        for j in range (cols):
            a = int(i*np.cos(rot) - j * np.sin(rot))
            b = int(i*np.sin(rot)+j*np.cos(rot))
            if a > rows or a < 0: a = 0
            if b > cols or b < 0: b = 0
            out[i,j] = img[a, b]
    return out

cv2.namedWindow('Rotacao')
cv2.setMouseCallback('Rotacao', click)

out = img 
rot = 0

while(1):
    cv2.imshow('Rotacao', out)
    
    key = cv2.waitKey(20) & 0xFF
    
    if key == ord('r'):
       rot += 10
       out = rotateImg(rot)
       
    if key == ord('q'):
        break
    
cv2.destroyAllWindows()