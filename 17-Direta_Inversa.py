import cv2
import numpy as np
import math

img = cv2.imread("ifma-caxias.jpg")

(rows, cols) = img.shape[0:2]


def rotateDirect(rot):
    # matiz de rotacao
    angule = np.radians(rot)
    mtx = [[np.cos(angule),np.sin(angule)],[-np.sin(angule),np.cos(angule)]]
    out = np.zeros(img.shape, np.uint8)
    for i in range (0, rows):
        for j in range (0, cols):
            # produto de matrizes
            (a,b) = (np.matmul([i,j], mtx)).astype(int) 
            # limite superior e inferior da matrix de pixels
            if (a >= 0) and (a < cols) and (b >= 0) and (b < rows):
                out[a,b] = img[i,j]
    return out

def rotateInverse(rot):
    angule = np.radians(rot)
    mtx = [[np.cos(angule),np.sin(angule)],[-np.sin(angule),np.cos(angule)]]
    # criando uma matriz inversa em python
    invr = np.linalg.inv(mtx)
    out = np.zeros(img.shape, np.uint8)
    for i in range (0, rows):
        for j in range (0, cols):
            # produto de matrizes
            (a,b) = (np.matmul([i,j], invr)).astype(int)
            # limite superior e inferior da matrix de pixels
            if (a >= 0) and (a < cols) and (b >= 0) and (b < rows):
                out[i,j] = img[b,a]
    return out
    

out = img 
out2 = img

while(1):
    cv2.imshow('Direta', out)
    cv2.imshow('Inversa', out2)
    
    key = cv2.waitKey(20) & 0xFF
    
    if key == ord('r'):
       rot += 10
       if rot > 360: rot = 0 
       out = rotateDirect(rot)
       out2 = rotateInverse(rot)
       
    if key == ord('q'):
        break
    
cv2.destroyAllWindows()