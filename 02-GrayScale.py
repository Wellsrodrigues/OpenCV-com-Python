import cv2

img = cv2.imread("logo-if.jpg")

# print(img.shape)
# shape retorna altura, largura e canais de cores

(row, col) = img.shape[0:2]

# print(img[0,0])
# cor de um pixel na imagem

# aplicando cinza manualmente pegando a media das cores, pois no cinza todas as cores são iguais
for i in range (row):
    for j in range (col):
        img[i,j] = sum(img[i,j]) * 0.33

cv2.imshow("Gray", img)

cv2.waitKey(0)
cv2.destroyAllWindows()