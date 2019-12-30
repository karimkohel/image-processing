#!/usr/bin/env python
import cv2
from skimage import measure

cap = cv2.VideoCapture(0)
img = cv2.imread("fingers.png")

while True:
	_, frame = cap.read()








	

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break



cap.release()
cv2.destroyAllWindows()