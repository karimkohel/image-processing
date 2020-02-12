import cv2
import numpy as np

img1 = cv2.imread("peace.jpg")
img1 = cv2.resize(img1, (200,200))

img2 = cv2.imread("pillow.jpg")
img2 = cv2.resize(img2, (200,200))

img3 = cv2.imread("morepillow.jpg")
img3 = cv2.resize(img3, (200,200))

filler = np.zeros([200,200,3], dtype=np.uint8)
filler.fill(255)


row1 = np.hstack([img1,filler])
row2 = np.hstack([img2,img3])

collage = np.vstack([row1, row2])

cv2.imshow("collage", collage)
cv2.waitKey(0)
cv2.destroyAllWindows()