import cv2
import numpy as np
import random

img = cv2.imread('logo-if.jpg')

def noise(image,prob):
    # criando uma nova imagem
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    # define a probabilidade
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                # pixel preto
                output[i][j] = 0
            elif rdn > thres:
                # pixel branco
                output[i][j] = 255
            else:
                # pixel normal
                output[i][j] = image[i][j]
    return output

noise = noise(img,0.03)
            
cv2.imshow('Salt & Pepper', noise)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
