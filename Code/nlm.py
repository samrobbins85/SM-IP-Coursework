import cv2 

##############################################################

# These parameter values are indicative. You should choose your own 
# according to properties of the method you want to demonstrate

h = 5
templateWindowSize = 7
searchWindowSize = 30

##############################################################

img = cv2.imread('alley-highNoise.png')

dst = cv2.fastNlMeansDenoisingColored(img, None, h, h, templateWindowSize, searchWindowSize)

cv2.imwrite('search30.png', dst)


