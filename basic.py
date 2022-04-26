import cv2 as cv

img= cv.imread('images/cat-large.jpg')

# converting image to grayscale
gray=cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)

# show in window
cv.imshow('Cat', gray)

# blurring an image
# remove noise from image, use gaussian blur, to increase blur-> increase kernel size (7,7)
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)

cv.imshow('blur', blur)

# edge cascade
# get rid of some edges using blur
canny=cv.Canny(blur, threshold1=125, threshold2=175)
cv.imshow('canny', canny)

# dilating the image
dilated=cv.dilate(canny, kernel=(7,7), iterations=3)
cv.imshow("dilated", dilated)

# eroding
eroded=cv.erode(dilated, kernel=(7,7), iterations=3)
cv.imshow("eroded", eroded)

# resize
# interpolation INTER_AREA useful if shrinking the image
resize=cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resize', resize)

# cropping
cropped=img[50:200,200:400]
cv.imshow("cropped", cropped)

cv.waitKey(0)