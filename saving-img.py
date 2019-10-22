import cv2

# learned that flag 0 == grayscale & 1 == color & -1 == color + alpha rays ? 
img = cv2.imread('arch-logo.png', 0)

cv2.imshow('Test', img)

key = cv2.waitKey(0)

if key == 27 or key == 113: # which are esc key and the char q in ascii
	pass
elif key == 115: # the letter s in ascii ( could have used the ord() method which takes in directly the letter -> ord('s'))
	cv2.imwrite('arch-logo-copy.png', img)

cv2.destroyAllWindows()