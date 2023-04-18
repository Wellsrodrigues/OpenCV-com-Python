import cv2

img = cv2.imread('logo-if.jpg')

#Redimensiona imagem
img = cv2.resize(img,(200,100),interpolation=cv2.INTER_AREA)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, mask_inv = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
mask = cv2.bitwise_not(mask_inv)

cv2.imshow('Original',img)
cv2.imshow('Grayscale',gray)
cv2.imshow('Threshold',mask)
cv2.imshow('Mask Inv',mask_inv)

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