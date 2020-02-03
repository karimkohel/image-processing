#!/usr/bin/env python
import cv2
from time import sleep

############### INITs ###############

cap = cv2.VideoCapture(0)

i = 0

side = ["Top.png", "Side1.png", "Side2.png", "Side3.png", "Side4.png"]

############### F(x) ###############

# for the trackbars
def empty():
	pass
	#just pass

# keep taking photos?
def take_photos(frame, x, y, w, h):

	if x < 0:
		print("no rectangles in sight?")
		return True, -1

	global i

	cv2.imwrite(side[i], frame)

	
	rows = frame.shape[0]
	columns = frame.shape[1]

	while True:
		degree = cv2.getTrackbarPos("rotation", "window")
		matrix = cv2.getRotationMatrix2D((x+w/2, y+h/2), degree, 1)
		rotated = cv2.warpAffine(frame, matrix, (columns,rows))
		cv2.imshow("rotation", rotated)

		newk = cv2.waitKey(3)

		if newk == ord('s'):
			break
		elif newk == ord("q"):
			print("ok won't save")
			return True, -1
		else:
			continue

	cv2.destroyWindow("rotation")

	cropped = rotated[y:y+h, x:x+w]

	print("->saving " + side[i])
	cv2.imwrite("Cropped"+side[i], cropped)

	i += 1

	if i == 5:
		return False, -1
	else:
		return True, rotated

############### MAIN ###############

cv2.namedWindow("window")
cv2.createTrackbar("thresh1", "window", 60, 255, empty)
cv2.createTrackbar("thresh2", "window", 50, 255, empty)
cv2.createTrackbar("rotation", "window", 0, 360, empty)

while True:
	succes, frame = cap.read()

	imgblur = cv2.GaussianBlur(frame, (5,5), 1)
	imggray = cv2.cvtColor(imgblur, cv2.COLOR_BGR2GRAY)
	imggray = cv2.bilateralFilter(imggray, 1, 10, 120 )

	thresh1 = cv2.getTrackbarPos("thresh1", "window")
	thresh2 = cv2.getTrackbarPos("thresh2", "window")
	imgedge = cv2.Canny(imggray, thresh1, thresh2)

	kernel = cv2.getStructuringElement( cv2.MORPH_RECT, (7, 7))
	imgDil = cv2.morphologyEx(imgedge, cv2.MORPH_CLOSE, kernel)

	contours, _ = cv2.findContours(imgDil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	for cnt in contours:
		area = cv2.contourArea(cnt)
		approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt,True), True)

		if area > 1500 and len(approx) == 4:
			x,y,w,h = cv2.boundingRect(approx)
			cv2.drawContours(frame, [approx], -1, (0,255,0), 3)
			break # found the contour so break out of the for loop

		else:
			x,y,w,h = -1,-1,-1,-1

	
	k = cv2.waitKey(5)

	if k == ord('s'):
		print("Sure ?")
		sleep(2)
		if cv2.waitKey(1) & 0xFF == ord('s'):
			keep_going, cropped = take_photos(frame, x, y, w, h)

			if not keep_going:
				print("finished all 5 photos and exiting")
				break
		else:
			print("Didn't save")

	elif k == ord('q'):
		print("Are you sure you want to exit ?")
		sleep(2)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			print("exiting")
			break
		print("Will continue")

	cv2.imshow("feed", frame)
	cv2.imshow("edge", imgDil)


print("Goodbye.")
cap.release()
cv2.destroyAllWindows()
exit()

"""
to do:

	-stitch the goddamn photos
	
"""