import cv2 
import numpy as np 

logo = cv2.imread('logo-if.jpg')

logo = cv2.resize(logo,(200,100),interpolation=cv2.INTER_AREA)

rows, cols, channels = logo.shape

# thresholding aplicado em escala de cinza
gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask_inv = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
mask = cv2.bitwise_not(mask_inv)
    
def fun_thresholding():
    # recorte do frame de fundo
    roi = frame[0:rows, 0:cols]

    # operacoes logicas
    img2 = cv2.bitwise_and(roi, roi, mask=mask_inv)
    img3 = cv2.bitwise_and(logo, logo, mask=mask)
    dts = cv2.add(img2,img3)

    # remontando img original com a parte modificada
    frame[0:rows, 0:cols] = dts
    return frame
    
cap = cv2.VideoCapture('IFMA Campus Caxias.mp4')

# aplicando para imagem
# frame = cv2.imread("ifma-caxias.jpg")
# result = fun_thresholding()
# cv2.imshow("Teste", result)
# cv2.imwrite("ifma-impainting.png", result)

while True:
    ret, frame = cap.read()

    if ret == True:
        res = fun_thresholding()
        cv2.imshow('Video', res)
       
        k = cv2.waitKey(50) & 0xFF
        if k == ord('m'):
            break
    else:
        break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
