import cv2 
import numpy as np 

img = cv2.imread('ifma-caxias.jpg')
logo = cv2.imread('logo-if.jpg')

logo = cv2.resize(logo,(200,100),interpolation=cv2.INTER_AREA)

rows, cols, channels = logo.shape

# recorte da imagem de fundo
roi = img[0:rows, 0:cols]

# thresholding aplicado em escala de cinza
gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask_inv = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
mask = cv2.bitwise_not(mask_inv)

# operacoes logicas
img2 = cv2.bitwise_and(roi, roi, mask=mask_inv)
img3 = cv2.bitwise_and(logo, logo, mask=mask)
dts = cv2.add(img2,img3)

# remontando img original com a parte modificada
img[0:rows, 0:cols] = dts

cv2.imshow("Mask", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
