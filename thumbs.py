#!/usr/bin/env python


import cv2
import numpy as np
from frameRate import FrameRate


cap = cv2.VideoCapture(0)


def smooth(img):
    kernel=np.ones((9,9)) 
    f2=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    f2 = cv2.GaussianBlur(f2, (21,21), 0)
    #f2 = cv2.morphologyEx(f2, cv2.MORPH_OPEN, kernel, iterations=3)
    return f2

showFR=FrameRate()

success, frame = cap.read()
orig = smooth(frame)

while True:
    success, frame = cap.read()
    if success != True:
        break


    f2=smooth(frame)
    cv2.imshow("blurred", f2)
    dist = np.array(f2, dtype=np.float32) - np.array(orig, np.float32)
    mask=np.zeros((480,640), dtype=np.uint8)
    mask[np.abs(dist) > 9]=255
    changed = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("mask", mask)
    cv2.imshow("changed", changed)

    fast=cv2.FastFeatureDetector(threshold=4)
    kp=fast.detect(mask,None)
    top=0
    bot=0
    if len(kp) > 10:
        for i in kp:
            if i.pt[1] > frame.shape[0]/2:
                top +=1
            else:
                bot +=1
    if top > bot:
        print "cooperate"
    elif bot > top:
        print "defect"

    frame=cv2.drawKeypoints(frame, kp, color=(255,0,0))

    out=showFR.write(frame)

    cv2.imshow("main", out)
    key = cv2.waitKey(10) & 0xff
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()

