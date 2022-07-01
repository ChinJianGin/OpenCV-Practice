import cv2 as cv

img = cv.imread('Photos/lake.jpg')
cv.imshow('Lake', img)

average = cv.blur(img, (9,9))
cv.imshow('Average Blur', average)

gauss = cv.GaussianBlur(img, (9, 9), 0)
cv.imshow('Gaussin Blur', gauss)

median = cv.medianBlur(img,5)
cv.imshow('Median Blur', median)

bilateral = cv.bilateralFilter(img, 5, 15, 60)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
cv.destroyAllWindows()