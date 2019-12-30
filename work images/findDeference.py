from skimage import measure
import matplotlib.pyplot as plt 
import numpy as np
import cv2

def mse(imgA, imgB):
	err = np.sum((imgA.astype("float") - imgB.astype("float")) ** 2)
	err /= float(imgA.shape[0] * imgB.shape[1])
	return err

def compareImages(imgA, imgB, title):
	m = mse(imgA, imgB)
	s = measure.compare_ssim(imgA, imgB)
	fig = plt.figure(title)
	m = round(m, 2)
	s = round(s, 2)
	plt.suptitle(f"MSE: {m}, SSIM: {s}")
	ax = fig.add_subplot(1,2,1)
	plt.imshow(imgA, cmap = plt.cm.gray)
	plt.axis("off")
	ax = fig.add_subplot(1,2,2)
	plt.imshow(imgB, cmap = plt.cm.gray)
	plt.axis("on")
	plt.show()


original = cv2.imread("jp_gates_original.png", 0)
contrast = cv2.imread("jp_gates_contrast.png", 0)
shopped = cv2.imread("jp_gates_photoshopped.png", 0)
fig = plt.figure("Images")
images = ("Original", original), ("contrast", contrast), ("Photoshoped", shopped)

for (i, (name, images)) in enumerate(images):
	ax = fig.add_subplot(1,3,i+1)
	ax.set_title(name)
	plt.imshow(images, cmap=plt.cm.gray)

compareImages(original, original, "Original, original")
compareImages(original, contrast, "Original , contrast")
compareImages(original, shopped, "Original , shopped")

cv2.waitKey(0)
cv2.destroyAllWindows()
