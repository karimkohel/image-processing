#!/usr/bin/env python
import cv2
from skimage import measure
import imutils

cap = cv2.VideoCapture(0)
img_gray = cv2.imread("pic1.png", 0)
img = cv2.imread("pic1.png")

while True:
	_, frame = cap.read()

	frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	(score, diff) = measure.compare_ssim(img_gray, frame_gray, full=True)#we won't use the score
	diff = (diff * 255).astype("uint8") # converting the float score from a (-1,1) range to 8 bit 0-255 range

	thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1] #still no clue why we using elemnt 1 of that list

	contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	contours = imutils.grab_contours(contours)



	for cnt in contours:
		area = cv2.contourArea(cnt)
		if 3150 < area:
			(x,y,w,h) = cv2.boundingRect(cnt)
			cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0))

	cv2.imshow("Current", frame)
	cv2.imshow("Back then", img)
	cv2.imshow("mask", thresh)


	if cv2.waitKey(1) & 0xFF == ord('q'):
		break



cap.release()
cv2.destroyAllWindows()