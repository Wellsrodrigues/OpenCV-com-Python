import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('atividade_aula11.png', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img,(200,200), interpolation = cv2.INTER_CUBIC)

# Img1: erosao
kernel_e = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
erosion_e = cv2.erode(img, kernel_e, iterations=4)


# Img2: dilatacao
kernel_d = cv2.getStructuringElement(cv2.MORPH_RECT,(41,51))
erosion_d = cv2.erode(img, kernel_d)
dilation_d = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))
dilated_d = cv2.dilate(erosion_d, dilation_d)


# Img 3: hiper dilatacao
kernel_h = cv2.getStructuringElement(cv2.MORPH_RECT,(9,9))
dilated_h = cv2.dilate(img, (kernel_h), iterations=5)
kernel_hp = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,9))
eroded_h= cv2.erode(dilated_h, kernel_hp, iterations=5)
dilation_h = cv2.dilate(eroded_h, kernel_hp, iterations=3)


plt.subplot(221), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Imagem')
plt.subplot(222), plt.imshow(cv2.cvtColor(erosion_e, cv2.COLOR_BGR2RGB))
plt.title('Erosão')
plt.subplot(223), plt.imshow(cv2.cvtColor(dilated_d, cv2.COLOR_BGR2RGB))
plt.title('Dilatação')
plt.subplot(224), plt.imshow(cv2.cvtColor(dilation_h, cv2.COLOR_BGR2RGB))
plt.title('Hiper Dilatação')

plt.tight_layout()
plt.show()