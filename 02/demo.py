import cv2

def main():
	imgpath = "D:\\OpenCv_Course\\Databases of Images for Computer Vision Programming\\misc\\4.1.01.tiff"
	img = cv2.imread(imgpath)
	#img = cv2.imread(imgpath, 0)
	#img = cv2.imread(imgpath, -1)

	outpath = "D:\\OpenCv_Course\\02\\Output\\lena.jpg"

	cv2.imshow('Lena', img)
	cv2.imwrite(outpath, img)
	cv2.waitKey(0)
	cv2.destroyWindow('Lena')
if __name__ == "__main__":
	main()