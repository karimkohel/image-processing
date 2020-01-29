#!/usr/bin/env python3

import cv2


cap = cv2.VideoCapture(1)

while True:
	ret, frame = cap.read()
	cv2.imshow('frame', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		cv2.imwrite("fingers.png", frame)
		break
	elif cv2.waitKey(1) & 0xFF == ord('s'):
		cv2.imwrite("fingers.png", frame)
		break

cap.release()
cv2.destroyAllWindows()