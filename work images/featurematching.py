#!/usr/bin/env python
import cv2

img1 = cv2.imread("co.png", 0)
img2 = cv2.imread("cf.png", 0)


orb = cv2.ORB_create()

kp1, des1 = orb.
kp2, des2 = orb.detectAndcompute(img2, None)

brutforce = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = brutforce.match(des1, des2)

print(len(matches))


cv2.imshow("original", img1)
cv2.imshow("feed", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()