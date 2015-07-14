#!/usr/bin/env python


import cv2
from frameRate import FrameRate


cap = cv2.VideoCapture(0)


showFR=FrameRate()
dim=(640,480)
codec = cv2.cv.CV_FOURCC('D','I','V','X')
avi = cv2.VideoWriter('output.avi',codec, 24.0, dim)

while True:
    success, frame = cap.read()
    if success != True:
        break

    print frame.shape

    out=showFR.write(frame)
    avi.write(out)

    cv2.imshow("main", out)
    key = cv2.waitKey(10) & 0xff
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()
out.release()

