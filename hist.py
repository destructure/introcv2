#!/usr/bin/env python


import cv2
import numpy as np
from frameRate import FrameRate


cap = cv2.VideoCapture(0)

def hist_curve(im,mask=None):
    bins = np.arange(256).reshape(256,1)
    h = np.zeros((300,256,3))
    if len(im.shape) == 2:
        color = [(255,255,255)]
    elif im.shape[2] == 3:
        color = [ (255,0,0),(0,255,0),(0,0,255) ]
    for ch, col in enumerate(color):
        hist_item = cv2.calcHist([im],[ch],mask,[256],[0,256])
        cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX)
        hist=np.int32(np.around(hist_item))
        pts = np.int32(np.column_stack((bins,hist)))
        cv2.polylines(h,[pts],False,col)
    y=np.flipud(h)
    y=cv2.resize(y, (0,0), fx=2, fy=2)
    return y



showFR=FrameRate()

while True:
    success, frame = cap.read()
    if success != True:
        break


    hist = hist_curve(frame)
    #frame = cv2.Sobel(frame, 3, 3, 5)
    out=showFR.write(frame)

    cv2.imshow("main", out)
    cv2.imshow("histogram", hist)
    key = cv2.waitKey(10) & 0xff
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()

