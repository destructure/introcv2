#!/usr/bin/env python


import cv2
import numpy as np
from frameRate import FrameRate


cap = cv2.VideoCapture(0)


showFR=FrameRate()

while True:
    success, frame = cap.read()
    if success != True:
        break


    kernel=np.ones((5,5)) 
    #frame = cv2.GaussianBlur(frame, (5,5), 0)
    frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)

    cv2.imshow("blurred", frame)
    edges = cv2.Canny(frame, 50, 150 )
    ecolor=cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    frame=cv2.bitwise_and(frame, ecolor)

    out=showFR.write(frame)

    cv2.imshow("main", out)
    key = cv2.waitKey(10) & 0xff
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()

