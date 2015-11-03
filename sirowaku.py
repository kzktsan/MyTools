import cv2
import numpy as np

white = cv2.imread("white.png")
img = cv2.imread("moto.png")

height = img.shape[0]
width = img.shape[1]

space = 63

for y in range(0, height) :
	for x in range(0, width) :
		white[y + space, x + space, 0:3] = img[y, x, 0:3]

up = img[0 : space , 0 : width]
down = img[height - space : height , 0 : width]
left = img[0 : height, 0 : space]
right = img[0 : height, width - space : width]
up_left = img[0:space, 0:space]
up_right = img[0:space, width-space:width]
down_left = img[height-space: height, 0:space]
down_right = img[height-space:height, width-space:width]

up = cv2.flip(up, 0)
down = cv2.flip(down, 0)
left = cv2.flip(left, 1)
right = cv2.flip(right, 1)
up_left = cv2.flip(up_left, -1)
up_right = cv2.flip(up_right, -1)
down_left = cv2.flip(down_left, -1)
down_right = cv2.flip(down_right, -1)

white[0:space, space:width+space] = up[0:space, 0:width]
white[height+space:height+(space*2), space:width+space] = down[0:space, 0:width]
white[space:height+space, 0:space] = left[0:height, 0:space]
white[space:height+space, width+space:width+(space*2)] = right[0:height, 0:space]
white[0:space, 0:space] = up_left[0:space, 0:space]
white[0:space, width+space:width+(space*2)] = up_right[0:space, 0:space]
white[height+space:height+(space*2), 0:space] = down_left[0:space, 0:space]
white[height+space:height+(space*2), width+space:width+(space*2)] = down_right[0:space, 0:space]

cv2.imwrite("wakutuki.png", white)
