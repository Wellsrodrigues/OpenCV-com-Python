import cv2
import numpy as np

img = cv2.imread("logo-if.jpg")

(row,col) = img.shape[0:2]

global lux, contrs
lux = 0 
contrs = 0


def brilho():
    shine = [lux, lux, lux]
    out = np.zeros(img.shape, np.uint8)
    for i in range (row):
        for j in range (col):
            out[i,j] = np.minimum(img[i,j]+shine,[255,255,255])
    return out
            
def negativo():
    for i in range (row):
        for j in range (col):
            img[i,j] = 255 - img[i,j]

def contrast():
    cont = [contrs, contrs, contrs]
    out = np.zeros(img.shape, np.uint8)
    for i in range (row):
        for j in range (col):
            out[i,j] = np.minimum(img[i,j]*cont,[255,255,255])
    return out
            
image = img
         
while(1):
    cv2.imshow("Resultado", image)
     
    key = cv2.waitKey(20) & 0xFF 
    
    # brilho
    if key == ord('a'):
        lux += 50
        if lux > 255: lux = 255
        image = brilho()
    
    if key == ord('z'):
        lux -= 50
        if lux < 0: lux = 0
        image = brilho()
        
     # contraste
    if key == ord('s'):
        contrs += 1
        if contrs > 255: contrs = 255
        image = contrast()
    
    if key == ord('x'):
        contrs -= 1
        if contrs < 0: contrs = 0
        image = contrast()
    
    # negativo
    if key == ord('n'):
        negativo()
    
    # exit
    if key == ord('q'):
        break
        
cv2.waitKey(0)
cv2.destroyAllWindows()