import cv2 as cv
import numpy as np

img = cv.imread('Photos/lake.jpg')
cv.imshow('Lake', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

center_x = img.shape[1]//2
center_y = img.shape[0]//2
circle = cv.circle(blank.copy(), (center_x-200, center_y-200), 125, 255, -1)
cv.imshow('Circle', circle)

rectangle = cv.rectangle(blank.copy(), (center_x - 300, center_y - 300), (center_x - 100,center_y - 100), 255, -1)
cv.imshow('Rectangle', rectangle)

weird_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('Weird Shape', weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Weird Shaped Masked Image', masked)


cv.waitKey(0)
cv.destroyAllWindows()