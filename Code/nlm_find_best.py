import cv2
import math
import numpy
import itertools

##############################################################

# These parameter values are indicative. You should choose your own 
# according to properties of the method you want to demonstrate

h = 3
templateWindowSize = 10
searchWindowSize = 21


##############################################################

img = cv2.imread('alley-highNoise.png')
original = cv2.imread('alley.png')
def psnr_diff(h, templateWindowSize, searchWindowSize):
	global img
	global original

	def psnr(img1, img2):
		mse = numpy.mean((img1 - img2) ** 2)
		if mse == 0:
			return 100
		PIXEL_MAX = 255.0
		return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

	dst = cv2.fastNlMeansDenoisingColored(img, None, h, h, templateWindowSize, 21)

	# cv2.imwrite('alley-noise-reduced.png', dst)

	return psnr(original, dst)


a = [list(range(1, 10)),list(range(1, 10)),list(range(1, 10))]
b=list(itertools.product(*a))
best_psnr=100
best_h=0
best_templateWindowSize = 0
best_searchWindowSize = 0
for item in b:
	score=psnr_diff(item[0],item[1],item[2])
	if score<best_psnr:
		best_psnr=score
		best_h=item[0]
		best_templateWindowSize=item[1]
		best_searchWindowSize=item[2]

print(best_psnr)
print(best_h)
print(best_templateWindowSize)
print(best_searchWindowSize)

