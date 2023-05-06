import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('atividade_aula11.png',0)

# kernel = np.ones((21,21),np.uint8)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(31,31))

dilation = cv2.dilate(img,kernel,iterations = 3)
erosion = cv2.erode(img,kernel,iterations = 3)
grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)


plt.subplot(221), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Imagem')
plt.subplot(222), plt.imshow(cv2.cvtColor(dilation, cv2.COLOR_BGR2RGB))
plt.title('Dilatin')
plt.subplot(223), plt.imshow(cv2.cvtColor(erosion, cv2.COLOR_BGR2RGB))
plt.title('Erosion')
plt.subplot(224), plt.imshow(cv2.cvtColor(grad, cv2.COLOR_BGR2RGB))
plt.title('Gradient')

plt.tight_layout()
plt.show()