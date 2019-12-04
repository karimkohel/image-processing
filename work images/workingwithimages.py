#!/usr/bin/env python3
import cv2
import numpy as np 

sora = cv2.imread("car.jpg",0)

image, contour = cv2.findContours(sora, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img = cv2.drawContours(image, contour, -1, (0,255,0), 3)

cv2.imshow("sora",img)

cv2.waitKey(0)
cv2.destroyAllWindows()