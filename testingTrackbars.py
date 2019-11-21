#!/usr/bin/env python3

import cv2
import numpy as np

def nth(x):
	print(x)


cap = cv2.VideoCapture(0)

cv2.namedWindow("Trackbars")

cv2.createTrackbar('L-H', "Trackbars", 50, 179, nth)
cv2.createTrackbar('L-S', "Trackbars", 50, 255, nth)
cv2.createTrackbar('L-V', "Trackbars", 50, 255, nth)
cv2.createTrackbar('U-H', "Trackbars", 50, 179, nth)
cv2.createTrackbar('U-S', "Trackbars", 50, 255, nth)
cv2.createTrackbar('U-V', "Trackbars", 50, 255, nth)


while True:
	_, frame = cap.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


	LH = cv2.getTrackbarPos('L-H', 'Trackbars')
	LS = cv2.getTrackbarPos('L-S', 'Trackbars')
	LV = cv2.getTrackbarPos('L-V', 'Trackbars')
	UH = cv2.getTrackbarPos('U-H', 'Trackbars')
	US = cv2.getTrackbarPos('U-S', 'Trackbars')
	UV = cv2.getTrackbarPos('U-V', 'Trackbars')



	min = np.array([LH,LS,LV])
	max = np.array([UH,US,UV])

	mask = cv2.inRange(hsv, min, max)

	res = cv2.bitwise_and(frame, frame,mask=mask)


	cv2.imshow("original", frame)
	cv2.imshow("mask", mask)
	cv2.imshow("result", res)
	key = cv2.waitKey(1)
	if key == 27:
		break

cap.release()
cv2.destroyAllWindows()