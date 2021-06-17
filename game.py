import cv2
import numpy as np
import sys
import time

cascPath = "haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
cap = cv2.VideoCapture(0)
W = 400
# H = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# W = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
def my_filled_circle(img, center):
    thickness = -1
    line_type = 8
    cv2.circle(img,center,W //8,(0, 0, 255),thickness,line_type)
z = 0
k = 100
co = 0
cx =100
count = 0 
while True:
    ret,frame= cap.read()
    frame = cv2.flip(frame,1)
    faces = faceCascade.detectMultiScale(frame, 1.1, 4)
    for (x, y, w, h) in faces:
        cex = x + w//2
        ceny = y + h//2    
        center = (cex,ceny)
        ellips = cv2.ellipse(frame, center, (50, 50), 0, 0, 360, (255, 0, 255), 4)
    if 1280>co>=640:
        z=z-1
    elif 0<=co<640:
        z=z+1
    elif co>=1280:
        co = 0
        z = 1
    if 100<cx<380:
        k=k+1
    elif k==309:
        print("Game Over")
        k,z = 0
        cx = 100
        co = 0
        count = 0
    elif 380<cx<660:
        k=k-1
    elif cx>=660:
        cx = 100
        k=101
    if (0<(cex-z)<50) and (ceny-k)<50:
        z=z-30
        co= 640
        k=k-100
        cx= cx-30
        count = count +1
    if (0>(cex-z)>-50) and (ceny-k)<50:
        z=z+30
        co= 0
        k=k-100
        cx= cx-100
        count = count +1
    if z<0:
        z=0
        co = 0
    if k<100:
        k=100
        cx = 100
    my_filled_circle(frame,(z,k))    
    cv2.putText(frame, "Face Game", (200,30), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0))
    cv2.putText(frame, "Score {}".format(count), (450,30), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0))

    co = co+1
    cx = cx+1
    cv2.imshow('Ball Game',frame)

    print(z,co,k,cx)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
