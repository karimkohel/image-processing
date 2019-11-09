#!/usr/bin/env python3

import cv2
import numpy as np

img = cv2.imread("desk.jpg")
imgGray = cv2.imread("desk.jpg",0)

template = cv2.imread("port.jpg",0)

w, h = template.shape[::-1]

res = cv2.matchTemplate(imgGray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.73
location = np.where(res >= threshold)

for pt in zip(*location[::-1]):
	cv2.rectangle(img, pt, (pt[0]+w,pt[1]+h), (0,255,255), 2)

cv2.imshow("detected", img)

cv2.waitKey(0)
cv2.destroyAllWindows()