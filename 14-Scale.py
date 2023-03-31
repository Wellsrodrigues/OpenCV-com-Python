
import cv2

img = cv2.imread('logo-if.jpg')

# multiplicando a escala em N vezes
scale = 1.5
w,h=(int(scale*img.shape[0]), int(scale*img.shape[1]))

res1 = cv2.resize(img,(h,w), interpolation = cv2.INTER_CUBIC)
res2 = cv2.resize(img,(h,w), interpolation = cv2.INTER_NEAREST)
res3 = cv2.resize(img,(h,w), interpolation = cv2.INTER_LINEAR)
res4 = cv2.resize(img,(h,w), interpolation = cv2.INTER_AREA)
res5 = cv2.resize(img,(h,w), interpolation = cv2.INTER_LANCZOS4)
res6 = cv2.resize(img,(h,w), interpolation = cv2.INTER_LINEAR_EXACT)
# res7 = cv2.resize(img,(h,w), interpolation = cv2.INTER_MAX)
# res8 = cv2.resize(img,(h,w), interpolation = cv2.WARP_FILL_OUTLIERS)
# res9 = cv2.resize(img,(h,w), interpolation = cv2.WARP_INVERSE_MAP)

cv2.imshow('res1',res1)
cv2.imshow('res2',res2)
cv2.imshow('res3',res3)
cv2.imshow('res4',res4)
cv2.imshow('res5',res5)
cv2.imshow('res6',res6)
# cv2.imshow('res7',res7)
# cv2.imshow('res8',res8)
# cv2.imshow('res9',res9)

cv2.waitKey(0)
cv2.destroyAllWindows()