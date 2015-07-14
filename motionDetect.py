#!/usr/bin/env python


import cv2
import numpy as np
from frameRate import FrameRate
from time import time


cap = cv2.VideoCapture(0)


showFR=FrameRate()

# cooldown 
t=time()
def cool():
    global t
    retval=False
    dt=time()
    print dt - t
    if dt - t > 5:
        t=dt
        retval=True
    return retval

def simp(frame):
    gs=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    scaled = cv2.resize(gs, (16,12))
    return scaled
success, frame = cap.read()
last=frame
last = simp(frame)
caught=False
dim=(640,480)
codec = cv2.cv.CV_FOURCC('D','I','V','X')
mdetect = cv2.VideoWriter('output.avi',codec, 24.0, dim)

while True:
    success, frame = cap.read()
    if success != True:
        break

    scaled = simp(frame)
    #frame = cv2.resize(frame, (640,480), interpolation=cv2.INTER_NEAREST)
    diff = cv2.bitwise_xor(scaled, last)

    _, thresh = cv2.threshold(diff, 127, 255, cv2.THRESH_BINARY)
    mag=np.count_nonzero(thresh)
    
    cv2.imshow("diff", cv2.resize(thresh, (640,480)))
    if mag > 30: 
        if not caught:
            print "changed", mag
            caught=True
            cv2.imshow("changed", frame)
        mdetect.write(frame)
    else:
        #print "reset"
        caught=False
    #last=scaled.copy()
    out=showFR.write(frame)

    cv2.imshow("main", out)
    key = cv2.waitKey(10) & 0xff
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()
mdetect.release()

