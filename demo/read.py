import cv2 as cv
import numpy as np

img = cv.imread('Photos/lake.jpg')

cv.imshow('Image', img)

# Convert gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

#Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges", canny)

# Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=10)
cv.imshow("Dilating", dilated)

# Eroding
eroded = cv.erode(dilated, (7, 7), iterations=10)
cv.imshow("Eroded", eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[100:400, 200:600]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
cv.destroyAllWindows();