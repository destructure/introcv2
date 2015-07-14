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


while True:
    success, frame = cap.read()
    if success != True:
        break



    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    name=["hue", "saturation", "value"]
    for i in range(3):
        cv2.imshow(name[i], hsv[:,:,i] )

    hmap=hsv[:,:,0].astype(np.float32)
    hue=cv2.getTrackbarPos("hue", wn)
    width=cv2.getTrackbarPos("width", wn)
    bandpass=np.abs(hmap - hue) < width/2
    mask=np.zeros((480,640), np.uint8)
    mask[bandpass] = 255
    frame=cv2.bitwise_and(frame, frame, mask=mask)




    showFR.write(frame)
    cv2.imshow("main", frame)

    key = cv2.waitKey(10) & 0xff
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()

