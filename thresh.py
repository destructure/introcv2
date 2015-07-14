#!/usr/bin/env python


import cv2
from frameRate import FrameRate


cap = cv2.VideoCapture(0)


showFR=FrameRate()

while True:
    success, frame = cap.read()
    if success != True:
        break

    gs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    success, bw = cv2.threshold(gs, 127, 255, cv2.THRESH_BINARY)
    if success is None:
        break

    out=showFR.write(bw)
    cv2.imshow("main", out)
    key = cv2.waitKey(10) & 0xff
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()

