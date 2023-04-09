import cv2
import numpy as np
import math

img = cv2.imread("ifma-caxias.jpg")

(rows, cols) = img.shape[0:2]


point = []

def click(event,x,y,flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,0,255),-1)
        point.append(x)
        point.append(y)

# usando funcao getRotation 
def rotateImg(rot):
    M = cv2.getRotationMatrix2D(point, rot, 1)
    out = cv2.warpAffine(img, M, (cols, rows))
    return out
    
# aplicando pixel a pixel
# def rotateImg(rot):
#     out = np.zeros(img.shape, np.uint8)
#     for x in range (rows):
#         for y in range (cols):
#             x2 = int((x*np.cos(np.radians(rot))) - (y* np.sin(np.radians(rot))))
#             y2 = int((x*np.sin(np.radians(rot))) + (y*np.cos(np.radians(rot))))
#             limites:
#             if x2 > rows or x2 < 0: x2 = 0
#             if y2 > cols or y2 < 0: y2 = 0
#             out[x,y] = img[x2, y2]
#     return out


# usando matrizes 
# def rotateImg(rot):
#     out = np.zeros(img.shape, np.uint8)
#     angule = np.radians(rot)
#     mtx = [[np.cos(angule),np.sin(angule)],[-np.sin(angule),np.cos(angule)]]
#     for x in range (rows):
#         for y in range (cols):
#             prod = np.array([x,y]).dot(mtx)
#             out[x,y] = img[prod[0],prod[1]]
#     return out

cv2.namedWindow('Rotacao')
cv2.setMouseCallback('Rotacao', click)

out = img 
rot = 0

while(1):
    cv2.imshow('Rotacao', out)
    
    key = cv2.waitKey(20) & 0xFF
    
    if key == ord('r'):
       rot += 10
       if rot > 360: rot = 0 
       out = rotateImg(rot)
       
    if key == ord('q'):
        break
    
cv2.destroyAllWindows()