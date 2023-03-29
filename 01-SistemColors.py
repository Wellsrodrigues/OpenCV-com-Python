import cv2
import numpy as np

img = cv2.imread("logo-if.jpg")
 
# img = cv2.imread("img/logo-if.jpg", cv2.IMREAD_GRAYSCALE)
# pre-definir o sistema de cores

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
# converter sistemas de cores

# cv2.imshow("Original", img)

b, g, r = cv2.split(img)
# separar 3 canais de cores

# cv2.imshow("Red", r)
# cv2.imshow("Green", g)
# cv2.imshow("Blue", b)

# res = cv2.merge([r,g,b])
# cv2.imshow("RGB", res)


cv2.waitKey(0)
cv2.destroyAllWindows()