#!/usr/bin/env python


import cv2
import numpy as np
from frameRate import FrameRate


cap = cv2.VideoCapture(0)


showFR=FrameRate()

def noop(ignored):
    pass

wn="controls"
cv2.namedWindow(wn)
cv2.createTrackbar("hue", wn, 128, 255,  noop )
cv2.createTrackbar("width", wn, 10, 255, noop )

p0=0
p1=0
d0=0
d1=0
dd=0
def lomeq(rad):
    global p0, p1, d0, d1, dd
    d1 = -p0 *(dd/(p1-p0))
    d0 = -p1 *(dd/(p1-p0))
    dd = d1 - d0
    return dd


nSlots=30
history=np.zeros((nSlots,2))
slot=0

while True:
    slot += 1
    if slot >= nSlots:
        slot=0
    success, frame = cap.read()
    if success != True:
        break
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hmap=hsv[:,:,0].astype(np.float32)
    hue=cv2.getTrackbarPos("hue", wn)
    width=cv2.getTrackbarPos("width", wn)
    bandpass=np.abs(hmap - hue) < width/2
    mask=np.zeros((480,640), np.uint8)
    mask[bandpass] = 255
    #filtered=cv2.bitwise_and(frame, frame, mask=mask)
    obj=cv2.GaussianBlur(mask, (9,9), 0)
    cv2.imshow("obj", obj)
    circles = cv2.HoughCircles(obj, cv2.cv.CV_HOUGH_GRADIENT, dp=3, minDist=640)
    if circles is not None:
        x=np.zeros(len(circles[0]))
        rad=1
        for i, c in enumerate(circles[0]):
            ctr=tuple(c[0:2])
            rad=c[2]
            cv2.circle(frame, ctr, rad, (0,0,255), thickness=3  )
            x[i]=c[0]
        direction=int(x.mean())
        looming=(480/rad)
        if looming < 1 or looming > 100:
            continue
        history[slot,0]=direction
        history[slot,1]=looming
        avgx, avgl = history.mean(axis=0).astype(np.int)
        cv2.line(frame, (320, 480), (avgx,240), (255,255,0), avgl)






    showFR.write(frame)
    cv2.imshow("main", frame)

    key = cv2.waitKey(10) & 0xff
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()

