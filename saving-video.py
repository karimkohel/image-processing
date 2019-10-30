import cv2

vid = cv2.VideoCapture(0)

while True:
	ret, frame = vid.read() # assigning 2 variables at the same time

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # to convert the feed into grayscale for faster processing

	cv2.imshow('Camera', gray) # can use the frame variable to show normal color

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

vid.release()
cv2.destroyAllWindows()