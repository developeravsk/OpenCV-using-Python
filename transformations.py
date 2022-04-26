from turtle import width
import cv2 as cv
import numpy as np
from torch import diag_embed

img= cv.imread('images/cat-large.jpg')

# translation
def translate(img, x, y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# resized image because the image seems to be too large
resize=cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resize', resize)


# -x -> Left, -y -> Up , x -> Right, y -> Down    

translated=translate(resize, -100,-100)


# show in window
cv.imshow('Cat', translated)

# rotation
def rotate(img, angle, rotPoint=None):
    (height, width)=img.shape[:2]

    if(rotPoint is None):
        rotPoint=(width//2, height//2)

    rotMat=cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension=(width, height)

    return cv.warpAffine(img, rotMat, dimension)

rotated=rotate(resize, -45)
cv.imshow("rotated", rotated)

# resize image
resized=cv.resize(resize, (500,500), interpolation=cv.INTER_LINEAR)
cv.imshow("resized", resized)


# flipping image, 0-> vertical flip, 1-> horizontal flip, -1-> both
flip=cv.flip(resized, flipCode=-1)
cv.imshow("flipped", flip)

#cropping
cropped=img[200:400, 300:400]
cv.imshow("cropped", cropped)

cv.waitKey(0)