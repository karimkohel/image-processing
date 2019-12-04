#!/usr/bin/env python3

import cv2
import numpy as np

font = cv2.FONT_HERSHEY_COMPLEX

tri, rect, cir, squ = 0, 0, 0, 0

img = cv2.imread("rov1.jpg", 0)

_, thresh = cv2.threshold(img, 87, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:

	approx = cv2.approxPolyDP(cnt, 0.035 * cv2.arcLength(cnt,True), True)
	area = cv2.contourArea(cnt)

	if 1500 < area < 19000:
		cv2.drawContours(img, [approx], -1, (0,255,0), 3)

		if len(approx) == 3:
			tri += 1

		elif len(approx) == 4:
			(x,y,w,h) = cv2.boundingRect(approx)

			if w in range(h,h+10) or w in range(h-10, h):
				squ += 1
			else:
				rect += 1

		else:
			cir += 1

print(f"triangles : {tri}")
print(f"squares : {squ}")
print(f"rectangles : {rect}")
print(f"circles : {cir}")

cv2.imshow("shapes", img)
cv2.imshow("threshold", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()