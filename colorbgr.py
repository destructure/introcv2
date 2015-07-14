#!/usr/bin/env python


import cv2
import numpy as np
from frameRate import FrameRate


cap = cv2.VideoCapture(0)


showFR=FrameRate()

black=np.zeros((480,640), np.uint8)
while True:
    success, frame = cap.read()
    if success != True:
        break



    name=["blue", "green", "red"]
    for i in range(3):
        chan=frame[:,:,i]
        print chan.shape, black.shape
        combo=[black, black, black]
        combo[i]=chan
        print combo
        out=cv2.merge(combo)
        cv2.imshow(name[i], out)

    

    showFR.write(frame)
    cv2.imshow("main", frame)

    key = cv2.waitKey(10) & 0xff
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()

