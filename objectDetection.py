#!/usr/bin/env python3

import cv2

face = cv2.CascadeClassifier('frontalface.xml')
eye = cv2.CascadeClassifier('eye.xml')

cap = cv2.VideoCapture(0)

while True:
	_,frame = cap.read()
	grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face.detectMultiScale(grey, 1.3, 5)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
		roi_grey = grey[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]

		eyes = eye.detectMultiScale(roi_grey,)
		for (ex, ey, ew, eh) in eyes:
			cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,127,127),2)
	cv2.imshow("frame", frame)

	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()