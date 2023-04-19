import cv2
import numpy as np

img = cv2.imread('noise.jpg')

ksize=7

# medianBlur é mais indicado para filtar ruido sal e pimenta
median = cv2.medianBlur(img,ksize)

cv2.imshow('Img',img)

cv2.imshow('Median',median)

cv2.waitKey(0)
cv2.destroyAllWindows()