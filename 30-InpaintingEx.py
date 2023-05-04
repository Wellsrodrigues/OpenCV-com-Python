import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('ifma-impainting.png')
mask = cv2.imread('ifma-impainting.png',0)

# logo = cv2.imread("logo-if.jpg")

# col, rows = img.shape[0:2]

# construir a mascara: area de remoção branca e fundo preto
# # def mask():
    

telea = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
ns = cv2.inpaint(img,mask,3,cv2.INPAINT_NS)

plt.subplot(221), plt.imshow(img)
plt.title('Imagem')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.title('Máscara')
plt.subplot(223), plt.imshow(telea)
plt.title('TELEA')
plt.subplot(224), plt.imshow(ns)
plt.title('NS')

plt.tight_layout()
plt.show()