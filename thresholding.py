#!/usr/bin/env python3

import cv2

img1 = cv2.imread("book.jpg")

# applying threshold on image and placing that threshold in retval and threshold variables
#              threshold(img, the number for 1 above and 0 below, maximum color, thresholdtype)
retval, threshold = cv2.threshold(img1, 90, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 90, 255, cv2.THRESH_BINARY)

# orrrr use grayscale from start...
img2 = cv2.imread("book.jpg", cv2.IMREAD_GRAYSCALE)


gaused = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115,1)

cv2.imshow("Original", img1)
cv2.imshow("gaussed", gaused)
# cv2.imshow("thresholded",threshold)
# cv2.imshow("thresholded2",threshold2)


cv2.waitKey(0)
cv2.destroyAllWindows()