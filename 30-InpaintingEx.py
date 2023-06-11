import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('ifma-impainting.png')
mask = cv2.imread('ifma-impainting.png',0)

logo = cv2.imread("logo-if.jpg",0)
logo = cv2.resize(logo,(200,100),interpolation=cv2.INTER_AREA)

rows, cols = logo.shape[0:2]

# construir a mascara: area de remoção branca e fundo preto
def createMask():
    output = np.zeros(img.shape, np.uint8)
    for i in range (rows):
        for j in range (cols):
            # transformar logo em branco 
            if (logo[i,j] > 200):
                logo[i,j] = 0
            else:
                logo[i,j] = 255
            # adicionar logo branco no fundo preto para formar a mask
            output[i][j] = logo[i][j]
    # retorna a mask em grayscale
    
    return (cv2.cvtColor(output, cv2.COLOR_BGR2GRAY))

mask = createMask()

# funcoes de inpainting
telea = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
ns = cv2.inpaint(img,mask,3,cv2.INPAINT_NS)


plt.subplot(221), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original')
plt.subplot(222), plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title('Mask')
plt.subplot(223), plt.imshow(cv2.cvtColor(telea, cv2.COLOR_BGR2RGB))
plt.title('TELEA')
plt.subplot(224), plt.imshow(cv2.cvtColor(ns, cv2.COLOR_BGR2RGB))
plt.title('NS')

plt.tight_layout()
plt.show()