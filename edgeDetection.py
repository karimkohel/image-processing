#!/usr/bin/env python3
import cv2

cap = cv2.VideoCapture(0)

while True:
	_,frame = cap.read()

	laplication = cv2.Laplacian(frame, cv2.CV_64F)

	sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
	sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

	cv2.imshow("original", frame)
	cv2.imshow("laplication", laplication)
	cv2.imshow('X', sobelx)
	cv2.imshow('Y', sobely)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break




cv2.destroyAllWindows()
cap.release()