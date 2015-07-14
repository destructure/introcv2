#!/usr/bin/env python

import cv2
import numpy as np
from frameRate import FrameRate

def smooth(img):
    f2=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    f2 = cv2.GaussianBlur(f2, (21,21), 0)
    return f2

class Player:
    def __init__(self, num):
        self.num = str(num)
        self.cap=cv2.VideoCapture(num)
        self.fr=FrameRate()
        success, frame =self.cap.read()
        if success != True:
            raise Exception("cap failed")
        self.orig  = smooth(frame)

    def imshow(self, text, image):
        cv2.imshow(text + " " + self.num, image)
    def release(self):
        self.cap.release()
    
    def getAnswer(self):
        answer="none"
        success, frame = self.cap.read()
        if success != True:
            raise Exception("cap failed")
        f2=smooth(frame)
        f2=smooth(frame)
        #self.imshow("blurred", f2)
        dist = np.array(f2, dtype=np.float32) - np.array(self.orig, np.float32)
        mask=np.zeros((480,640), dtype=np.uint8)
        mask[np.abs(dist) > 9]=255
        #changed = cv2.bitwise_and(frame, frame, mask=mask)
        #self.imshow("mask", mask)
        #self.imshow("changed", changed)

        fast=cv2.FastFeatureDetector(threshold=4)
        kp=fast.detect(mask,None)
        top=0
        bot=0
        if len(kp) > 10:
            for i in kp:
                if i.pt[1] > frame.shape[0]/2:
                    top +=1
                else:
                    bot +=1
        if top > bot:
            answer="cooperate"
        elif bot > top:
            answer="defect"

        frame=cv2.drawKeypoints(frame, kp, color=(255,0,0))
        out=self.fr.write(frame)
        self.imshow("main", out)
        return answer

p0=Player(0)
p1=Player(1)

last=("none", "none")
score=[0,0]
while True:

    a0 = p0.getAnswer()
    a1 = p1.getAnswer()
    print a0, a1
    if (a0, a1) == last:
        if a0 == "cooperate" and a1 == "cooperate":
            score[0] += 2
            score[1] += 2
        elif a0 == "cooperate" and a1 == "defect":
            score[0] += 7
            score[1] += 1
        elif a0 == "defect" and a1 == "cooperate":
            score[0] += 1
            score[1] += 7
        elif a0 == "defect" and a1 == "defect":
            score[0] += 4
            score[1] += 4

    last = (a0, a1)
    sframe=np.zeros((100,400), np.uint8)
    face=cv2.cv.CV_FONT_HERSHEY_SIMPLEX
    scale=1
    text= "p0: %5d, p1 %5d" % tuple(score)
    cv2.putText(sframe,text, (20,40), face, scale, (255,255,255))
    cv2.imshow("score", sframe)
    key = cv2.waitKey(10) & 0xff
    if key == 27:
        break

cv2.destroyAllWindows()
p0.release()
p1.release()
