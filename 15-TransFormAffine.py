import cv2
import numpy as np

img = cv2.imread("ifma-caxias.jpg")

(rows, cols) = img.shape[0:2]

# Transformação afim: produtos de matrizes aplicadas a imagem final

# mtx1 = [[50,50],[200,50],[50,200]]
# mtx2 = [[10,100],[200,50],[100,250]]
# mxtF = cv2.getAffineTransform(np.float32(mtx1), np.float32(mtx2))

# rotação

# M = np.float32([[1,0,100],[0,1,50]])
# # cv2.getRotationMatrix2D(center, angle, scale)
# M = cv2.getRotationMatrix2D((100,100),90,1)

# imgF = cv2.warpAffine(img, M, (cols, rows))

# prespectiva: aplia a partir de 4 pontos selecionados
 
pts1 = [[200,100],[400,100],[50,400],[550,400]]
pts2 = [[0,0],[300,0],[0,300],[300,300]]
M = cv2.getPerspectiveTransform(np.float32(pts1),np.float32(pts2))

res = cv2.warpPerspective(img,M,(300,300))

# destancando os pontos
for pt in pts1:
    cv2.circle(img,pt,5,(0,0,255),-1)

for pt in pts2:
    cv2.circle(res,pt,5,(0,0,255),-1)

cv2.imshow('Original', img)
cv2.imshow('Transformada', res)

cv2.waitKey(0)
cv2.destroyAllWindows()