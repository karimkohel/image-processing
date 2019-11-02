#!/usr/bin/env python3

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()

	# hsv = hue saturation value
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lowerPink = np.array([150,50,40])
	upperPink = np.array([180,255,150])

	mask = cv2.inRange(hsv, lowerPink, upperPink)
	res = cv2.bitwise_and(frame, frame, mask=mask)

	# kernel = np.ones((15,15), np.float32) / 225
	# smoothed = cv2.filter2D(res, -1, kernel)

	# blur = cv2.GaussianBlur(res, (15,15), 0)

	median = cv2.medianBlur(res, 15)

	cv2.imshow("frame", frame)
	# cv2.imshow("mask", mask) dont need here
	cv2.imshow("res", res)
	# cv2.imshow("smoothed", smoothed)
	# cv2.imshow("blur", blur)
	cv2.imshow("median", median)



	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()