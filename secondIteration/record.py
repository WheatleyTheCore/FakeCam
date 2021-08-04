#!/usr/bin/env python3

import numpy as np
import cv2


def recordVideo():
    cap = cv2.VideoCapture(0)

    recording = np.empty((1800, 480, 640, 3), np.dtype('uint8')) #enough stoarage for 1 min of 30FPS footage

    for i in range(0, 1800):
        ret, bgrFrame = cap.read() #get frame from camera
        rgbFrame = cv2.cvtColor(bgrFrame, cv2.COLOR_BGR2RGB) #raw frame from camera is BGR, so convert to RGB
        cv2.imshow('frame',rgbFrame)
        recording[i] = rgbFrame

    cap.release()
    cv2.destroyAllWindows()

    with open('videos/video.npy', 'wb') as f: #save the video to file
        np.save(f, recording)

    with open('video.npy', 'rb') as f:
        rec = np.load(f)
        print(rec.shape)

recordVideo()
