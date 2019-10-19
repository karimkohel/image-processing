#!/usr/bin/env python3

import cv2

# # grayscale is much more faster to process, but i can use color if desirable
# img = cv2.imread('arch-logo.png',cv2.IMREAD_GRAYSCALE)

# cv2.imshow('img',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	cv2.imshow('frame', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()