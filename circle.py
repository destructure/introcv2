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


    kernel=np.ones((3,3)) 
    gs=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gs = cv2.GaussianBlur(gs, (21,21), 0)
    gs = cv2.morphologyEx(gs, cv2.MORPH_OPEN, kernel)
    cv2.imshow("blurred", gs)

    circles=cv2.HoughCircles(gs, cv2.cv.CV_HOUGH_GRADIENT, dp=3, minDist=100)
    if circles is not None:
        for c in circles[0]:
            ctr=tuple(c[0:2])
            rad=c[2]
            cv2.circle(frame, ctr, rad, color=(0,0,255), thickness=3 )

    out=showFR.write(frame)

    cv2.imshow("main", out)
    key = cv2.waitKey(10) & 0xff
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()

