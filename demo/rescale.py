import cv2 as cv

img = cv.imread('Photos/lake.jpg')
cv.imshow('Lake', img)

def rescaleImg(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resize_img = rescaleImg(img)
cv.imshow("Resize img", resize_img)

cv.waitKey(0)
cv.destroyAllWindows()