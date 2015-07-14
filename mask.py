#!/usr/bin/env python


import cv2
from frameRate import FrameRate


cap = cv2.VideoCapture(0)

itworked = cv2.imread("itworked.png")
mgs= cv2.cvtColor(itworked,cv2.COLOR_BGR2GRAY)
mgs = cv2.bitwise_not(mgs)

showFR=FrameRate()

while True:
    success, frame = cap.read()
    if success != True:
        break


    #frame=cv2.bitwise_and(frame, itworked)
    #frame=cv2.bitwise_and(frame, frame, mask=mgs)
    fgs=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    t, thresh = cv2.threshold(fgs, 127, 255, cv2.THRESH_BINARY)
    frame=cv2.bitwise_and(itworked, itworked, mask=thresh)
    out=showFR.write(frame)

    cv2.imshow("main", out)
    key = cv2.waitKey(10) & 0xff
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()

