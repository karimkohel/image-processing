#!/usr/bin/env python3

import cv2

img = cv2.imread('arch-logo.png', cv2.IMREAD_COLOR)

# to refrence a pixel
px = img[140,200] # the image is like a list of points and you choose the pixel as described 

# the pixel will hold its color value in BGR
print(px) 

# also you can modify a pixel like this

img[140,200] = [255,255,255]

px = img[140,200]
print(px)

# ROI = Region of image -> treated as a bunch of pixels
roi = img[100:150, 100:150]

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()