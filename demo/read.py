import cv2 as cv

img = cv.imread('Photos/printbackground.jpg')
cv.imshow('Image', img)
cv.waitKey(0)