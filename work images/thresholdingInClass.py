#!/usr/bin/env python

import cv2
# import numpy as np

def nth(x):
	pass

img = cv2.imread("car.jpg",0)

cv2.namedWindow("threshed")
cv2.createTrackbar('Threshold', "threshed", 0, 255, nth)

while True:
	threshold = cv2.getTrackbarPos("Threshold", "threshed")
	_,th1 = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
	cv2.imshow("original", img)
	cv2.imshow("threshed", th1)
	key = cv2.waitKey(1)
	if key == 27:
		break



cv2.destroyAllWindows()