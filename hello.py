#!/usr/bin/env python


# just see if cv2 is working


import cv2


frame = cv2.imread("itworked.png")

print frame.shape


cv2.imshow("main", frame)

cv2.waitKey()
