#!/usr/bin/env python


# just see if cv2 is working


import cv2
from time import time

def s2m(s):
        m=s/ 60
        s=s % 60
        return "%d:%02d" % (m,s)

class FrameRate:
    def __init__(self):
        self.nFrames=0
        self.start=time()
    def write(self, frame):
        passed=time()
        start=self.start
        nf=self.nFrames
        fps= "fps: %3.2f, t: %s" % (nf/(passed-start),s2m(passed-start))
        face=cv2.cv.CV_FONT_HERSHEY_SIMPLEX
        scale=1
        cv2.rectangle(frame, (0,0), (325,60),  (0,0,0),  -1)
        cv2.putText(frame, fps, (20,40), face, scale, (255,255,0))
        self.nFrames+=1
        return frame

if __name__ == "__main__":

    cap = cv2.VideoCapture(0)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.cv.CV_CAP_PROP_FPS, 30)

    showFR=FrameRate()
    while True:
        success, frame = cap.read()
        #print success, frame
        if success != True:
            break

        out=showFR.write(frame)
        cv2.imshow("main", frame)
        key = cv2.waitKey(10) & 0xff
        if key == 27:
            break

    cv2.destroyAllWindows()
    cap.release()
