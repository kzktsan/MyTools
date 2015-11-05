import cv2
import numpy as np

img1 = cv2.imread("mask.png")
img2 = cv2.imread("moto.png")

height = img1.shape[0]
width = img1.shape[1]

for y in range(0, height):
	for x in range(0, width):
		if img1[y,x,2] != 255 :
			img2[y,x,0:3] = 0

cv2.imwrite("result.png", img2)