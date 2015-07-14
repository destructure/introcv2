#!/usr/bin/env python


import cv2
from frameRate import FrameRate


cap = cv2.VideoCapture(0)


showFR=FrameRate()

while True:
    success, frame = cap.read()
    if success != True:
        break

    print frame.shape

    frame = cv2.resize(frame, (16,12))
    frame = cv2.resize(frame, (640,480), interpolation=cv2.INTER_NEAREST)
    out=showFR.write(frame)

    cv2.imshow("main", out)
    key = cv2.waitKey(10) & 0xff
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()

