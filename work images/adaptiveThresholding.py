#!/usr/bin/env python
import cv2
import numpy as np

img = cv2.imread("book.jpg", 0)

thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

cv2.imshow("original", img)
cv2.imshow("thresh", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()