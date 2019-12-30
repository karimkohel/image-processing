import cv2
from skimage import measure
import matplotlib.pyplot as plt
import numpy as np


imga = cv2.imread("original_01.png")
imgb = cv2.imread("modified_01.png")

original = cv2.imread("original_01.png", 0)
contrast = cv2.imread("modified_01.png", 0)

(score, diff) = measure.compare_ssim(original, contrast, full=True)

diff = (diff * 255).astype("uint8")
print(f"SSIM : {score}")

thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
	(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(imga, (x,y), (x+w, y+h), (0,255,0))
	cv2.rectangle(imgb, (x,y), (x+w, y+h), (0,255,0))

cv2.imshow("original", original)
cv2.imshow("modified", imgb)
cv2.imshow("diff", diff)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()