#!/usr/bin/env python3

import cv2
import numpy as np

def nothing(x):
	pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("test1")

cv2.createTrackbar('test', 'test1', 50, 500, nothing)
cv2.createTrackbar("colorToGray", 'test1', 0, 1, nothing)

while True:
	_, frame = cap.read()

	test = cv2.getTrackbarPos('test', 'test1')
	test2 = cv2.getTrackbarPos("colorToGray", 'test1')

	if test2 == 1:
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


	font = cv2.FONT_HERSHEY_COMPLEX
	cv2.putText(frame, str(test), (50,200), font, 1, (0,255,0))

	cv2.imshow("original", frame)

	key = cv2.waitKey(1)
	if key == 27:
		break

cap.release()
cv2.destroyAllWindows()