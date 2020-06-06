import numpy
import math
import cv2

def psnr(img1, img2):
	mse = numpy.mean((img1 - img2) ** 2)
	if mse == 0:
		return 100
	PIXEL_MAX = 255.0
	return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

img1 = cv2.imread('alley.png')
img2 = cv2.imread('template15.png')
print(psnr(img1,img2))