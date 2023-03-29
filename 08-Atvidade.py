from random import randint
import cv2
import os
import numpy as np

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)

COLORS=[BLUE,GREEN,RED,BLACK,GRAY]

key_color = 0

capture = cv2.VideoCapture("IFMA Campus Caxias.mp4")

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

history = []

def draw_circle(event,x,y,flags,param):
    print("circle")
    for (x,y,color) in history:
        cv2.circle(frame, (x,y), 10, color, -1) 

def click(event, x,y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        history.append((x,y,COLORS[key_color]))
        print(history)
        
cv2.namedWindow('window')
cv2.setMouseCallback('window', click)

if not capture.isOpened():
    print("Erro ao acessar camera")
else:
    # tipo de processamento de video
    fourcc = cv2.VideoWriter_fourcc(*'mpv4') 
    # copia do video frame a frame
    output = cv2.VideoWriter("backup.mp4", fourcc, int(fps), (int(frame_width), int(frame_height)), False)
   
    while capture.isOpened():
        check, frame = capture.read()
        if check is True:
            # desenhando em cada frame
            # cv2.circle(frame,(500, 300),50,cor,-1)
            
            key = cv2.waitKey(20) & 0xFF
            
            #mudando a cor
            c=randint(0,len(COLORS)-1)
            key_color = COLORS[c]
             
            if key == ord('c'):
                c=randint(0,len(COLORS)-1)
                key_color = COLORS[c]
        
            # salvando backup de frame
            output.write(frame)
            
            # exibindo video frame a frame
            cv2.imshow('window', frame)
            
            # teclas
            if key == ord('q'):
                break
            
            # deletar frame salvo
            if key == ord(' '):
                history.clear()
            
            # salvar frame   
            if key == ord('w'):
                print("Salvando frame...")
                cv2.imwrite('print.jpg',frame)
            
        else: break

capture.release()
output.release()
cv2.destroyAllWindows()
