#!/usr/bin/env python


# just see if cv2 is working


import cv2


cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if success != True:
        break
    print success, frame.shape
    cv2.imshow("main", frame)
    key = cv2.waitKey(10) & 0xff
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()
