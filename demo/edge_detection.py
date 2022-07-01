import cv2 as cv
from cv2 import Mat
from cv2 import BORDER_DEFAULT
import numpy as np

img = cv.imread('Photos/lake.jpg')
cv.imshow('Lake', img)

remove_noise = cv.GaussianBlur(img, (3,3), 0, 0, BORDER_DEFAULT)

gray = cv.cvtColor(remove_noise, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0 ,1)
abs_sobelx = cv.convertScaleAbs(sobelx)
abs_sobely = cv.convertScaleAbs(sobely)
combined_sobel = cv.bitwise_or(abs_sobelx, abs_sobely)

grad = cv.addWeighted(abs_sobelx, 0.5, abs_sobely, 0.5, 0)
cv.imshow('Added', grad)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)

cv.imshow('Abs Sobel X', abs_sobelx)
cv.imshow('Abs Sobel Y', abs_sobely)

cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)


cv.waitKey(0)
cv.destroyAllWindows()