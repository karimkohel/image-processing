#!/usr/bin/env python3

import cv2

img = cv2.imread('arch-logo.png', cv2.IMREAD_COLOR)

##drawing a line ; line(file, startpoint, endpoint, color in BGR, width in px)
# cv2.line(img, (0,0), (338,338), (255, 255, 255)) 

## drawing a rectangle 
cv2.rectangle(img, (150,130), (200,180), (0,255,0), 2)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Opencv is cool", (160,185), font, 0.6, (0,255,0), 1, cv2.LINE_AA)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
