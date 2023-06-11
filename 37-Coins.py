import cv2
import numpy as np

orig = cv2.imread('coins.jpeg')

gray = cv2.cvtColor(orig,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
res=orig.copy()

img_blur = cv2.medianBlur(orig,5)
img_blur = cv2.cvtColor(img_blur,cv2.COLOR_BGR2GRAY)

# identificando circulos
circles = cv2.HoughCircles(img_blur,cv2.HOUGH_GRADIENT,1,100,
                           param1=200,param2=50)
circles = np.uint16(np.around(circles))
   
# desenhando contornos
for i in circles[0,:]:
    cv2.circle(res,(i[0],i[1]),i[2],(0,0,255),2)  #bordas
    cv2.circle(res,(i[0],i[1]),5,(0,255,0),-1) #raio
    
cv2.imshow('Coins',res)

cv2.waitKey(0)
cv2.destroyAllWindows()