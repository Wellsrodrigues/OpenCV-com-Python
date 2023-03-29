import cv2
import numpy as np
import random

img = cv2.imread('logo-if.jpg', cv2.IMREAD_GRAYSCALE)

def reduce_center(image):
    (x,y)=(image.shape[0]//3,image.shape[1]//3)
    output = np.zeros((x,y),np.uint8)
    for i in range(1,x*3,3):
        for j in range(1,y*3,3):
            output[(i-1)//3][(j-1)//3] = image[i][j]
    return output

def reduce_mean(image):
    (x,y)=(image.shape[0]//3,image.shape[1]//3)
    output = np.zeros((x,y),np.uint8)
    for i in range(1,x*3,3):
        for j in range(1,y*3,3):
            output[(i-1)//3][(j-1)//3] = np.uint16(image[i-1:i+2,j-1:j+2]).sum()//9
    return output

img_center = reduce_center(img)
img_mean = reduce_mean(img)
            
cv2.imshow('Original', img)
cv2.imshow('Center', img_center)
cv2.imshow('Mean', img_mean)
 
cv2.waitKey(0)
cv2.destroyAllWindows()