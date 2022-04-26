import cv2 as cv

img= cv.imread('images/cat-large.jpg')

# show in window
cv.imshow('Cat', img)

# best practice to downscale the video than its original resolution
def rescale(frame, scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#resize image
resized_image=rescale(img)

# displaying the resized video
cv.imshow("Resized cat", resized_image)
# waits for infinite time for keyboard to be pressed
cv.waitKey(0)