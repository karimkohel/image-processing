#!/usr/bin/env python3
import cv2;


img = cv2.imread("shapes.jpg");
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);

_, thresh = cv2.threshold(imgray, 127, 255, 0);
cont, hir = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE);


cv2.imshow("original", imgray);
cv2.waitKey();
cv2.destroyAllWindows();
