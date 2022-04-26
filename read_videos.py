import cv2 as cv

# use 0,1,2,3 for web cam, default web cam 0, or else give absolute path
capture=cv.VideoCapture('videos/Messenger.mp4')


# best practice to downscale the video than its original resolution
# for existing media
def rescale(frame, scale=0.25):
    # works for images, video and live video
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# for live video
def changeRes(width, height):
    # 3 references to width, 4 references to height, brightness 10
    # works only for live video
    capture.set(3, width)
    capture.set(4, height)

#use while loop to read video frame by frame
while True:
    isTrue, frame=capture.read()

    frame_resized=rescale(frame)

    # display each frame of video
    # cv.imshow('Video', frame)

    #displaying resized video
    cv.imshow('Video', frame_resized)

    # if letter d is pressed get out of the loop
    if(cv.waitKey(20) & 0xFF==ord('d')):
        break
# error case:    
# -215 assertion failed error, video ran out of frames or could not find the media file at a particular location
capture.release()
cv.destroyAllWindows()