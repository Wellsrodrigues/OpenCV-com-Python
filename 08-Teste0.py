import cv2
import numpy as np

def draw_shape(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
       
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(frame, (ix, iy), (x, y), (0, 0, 0), 500)
            else:
                cv2.circle(frame, (x, y), 50, (0, 0, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(frame, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv2.circle(frame, (x, y), 50, (0, 0, 255), -1)

drawing = False
mode = True
ix, iy = -1, -1

cap = cv2.VideoCapture('IFMA Campus Caxias.mp4')

cv2.namedWindow('Video')
cv2.setMouseCallback('Video', draw_shape)

while True:
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow('Video', frame)
       
        k = cv2.waitKey(50) & 0xFF
        if k == ord('m'):
            mode = not mode
        elif k == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
