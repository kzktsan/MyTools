def bondim(img1, img2, img2_x, img2_y) :
	height = img1.shape[0]
	width = img1.shape[1]

	for y in range(img2_y-200, img2_y + 200) :
		for x in range(img2_x-200, img2_x + 200) :
			if (img2[y, x, 0] > 10) and (img2[y, x, 1] > 10) and (img2[y, x, 2] > 10) : 
				img1[y, x, 0:3] = img2[y, x, 0:3]

	return img1