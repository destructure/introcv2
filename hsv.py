#!/usr/bin/env python


import cv2
from frameRate import FrameRate


cap = cv2.VideoCapture(0)


showFR=FrameRate()

while True:
    success, frame = cap.read()
    if success != True:
        break



    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    name=["hue", "saturation", "value"]
    for i in range(3):
        cv2.imshow(name[i], hsv[:,:,i] )


    showFR.write(frame)
    cv2.imshow("main", frame)

    key = cv2.waitKey(10) & 0xff
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()

