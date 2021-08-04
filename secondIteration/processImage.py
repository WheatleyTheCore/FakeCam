#!/usr/bin/env python3
import numpy as np
import cv2

def processImage(frame):
    #essentially needs to make image into the correct size (640 x 480)

    CROPPED_WIDTH = 640
    CROPPED_HEIGHT = 480

    #get image dimensions
    height, width, _ = frame.shape

    midHeight = height//2
    midWidth = width//2

    topBound = midHeight + (CROPPED_HEIGHT // 2)
    bottomBound = midHeight - (CROPPED_HEIGHT // 2)
    leftBound = midWidth - (CROPPED_WIDTH // 2)
    rightBound = midWidth + (CROPPED_WIDTH // 2)


    croppedImage = frame[bottomBound:topBound, leftBound:rightBound]

    return croppedImage

