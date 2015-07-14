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


    kernel=np.ones((9,9)) 
    f2=frame
    f2 = cv2.GaussianBlur(f2, (21,21), 0)
    f2 = cv2.morphologyEx(f2, cv2.MORPH_OPEN, kernel, iterations=3)
    cv2.imshow("blurred", f2)

    fast=cv2.FastFeatureDetector(threshold=4)
    kp=fast.detect(f2,None)
    print len(kp)
    frame=cv2.drawKeypoints(frame, kp, color=(255,0,0))

    out=showFR.write(frame)

    cv2.imshow("main", out)
    key = cv2.waitKey(10) & 0xff
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()

