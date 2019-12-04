#!/usr/bin/env python3

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

i = 0

while True:
	_, frame = cap.read()

	blurred = cv2.GaussianBlur(frame, (5,5), 0)

	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	lowerBlue = np.array([88,135,45])
	upperBlue = np.array([118,229,246])
	mask = cv2.inRange(hsv, lowerBlue, upperBlue)


	contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

	for contour in contours:
		approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
		area = cv2.contourArea(contour)
		if area > 23000:
			cv2.drawContours(frame, [approx], -1, (0,255,0), 2)

			if len(approx) == 5:
				i += 1
				print(i)








	cv2.imshow("original", mask)
	# cv2.drawContours(frame, contours, -1, (0,255,0), 3)
	cv2.imshow("frame", frame)

	k = cv2.waitKey(1)
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()