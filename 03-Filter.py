import cv2
import copy

# mask no openCV

img = cv2.imread("original.jpeg")
img = cv2.resize(img, (300, 400))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, (300, 400))

final = copy.copy(img)

(row, col) = final.shape[0:2]

for i in range (row):
    for j in range (col):
        b = (final[i,j])[0]
        g = (final[i,j])[1]
        r = (final[i,j])[2]
        
        if(r > b > g):
              continue
        else:
            final[i,j] = sum(final[i,j]) * 0.33
            
cv2.imshow("BGR", img)
cv2.imshow("Gray", gray)
cv2.imshow("Final", final)

cv2.waitKey(0)
cv2.destroyAllWindows()