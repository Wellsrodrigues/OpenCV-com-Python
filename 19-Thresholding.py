import cv2
import numpy as np

fundo = cv2.imread('ifma-caxias.jpg')

overlay = cv2.imread('logo-if.jpg')


rows,cols = fundo.shape[0:2]

rows2, cols2 = overlay.shape[0:2]

def thresholding():
    for i in range (rows2):
        for j in range (cols2):
            fundo[i,j] = 0
    return fundo
    
    
res = thresholding()

cv2.imshow('IMG', res)
cv2.waitKey(0)
cv2.destroyAllWindows()