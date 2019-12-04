#!/usr/bin/env python3

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()

	# hsv = hue saturation value
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lowerblue = np.array([78,62,45])
	upperblue = np.array([110,237,200])

	mask = cv2.inRange(hsv, lowerblue, upperblue)
	res = cv2.bitwise_and(frame, frame, mask=mask)

	kernel = np.ones((5,5), np.uint8)

	opening = cv2.morphologyEx(res, cv2.MORPH_OPEN, kernel)


	cv2.imshow("frame", frame)
	# cv2.imshow("mask", mask)
	cv2.imshow("res", opening)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()