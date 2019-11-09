import cv2
import numpy as np 
sora=cv2.imread("car.jpg")
cv2.rectangle(sora,(25,30) ,(40,60) ,(0,255,0),2 )
cv2.imshow("sora",sora)
cv2.waitKey(0)
cv2.destroyAllWindows()