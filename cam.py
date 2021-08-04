#!/usr/bin/env python3

import time
import pyfakewebcam
import numpy as np
import cv2
import sys

inputSelection = int(sys.argv[1])

cameraCap = cv2.VideoCapture(0)

videoCap = cv2.VideoCapture('test.mp4')
frameCount = int(videoCap.get(cv2.CAP_PROP_FRAME_COUNT))
frameWidth = int(videoCap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(videoCap.get(cv2.CAP_PROP_FRAME_HEIGHT))

buf = np.empty((frameCount, 480, 640, 3), np.dtype('uint8'))

fc = 0
ret = True

while (fc < frameCount  and ret):
    ret, frame = videoCap.read()
    frame = frame[30:510, 160:800]
    buf[fc] = frame
    fc += 1

videoCap.release()

camera = pyfakewebcam.FakeWebcam('/dev/video2', 640, 480)


if inputSelection == 0:
    while True:
        ret, frame = cameraCap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        camera.schedule_frame(rgb)
        time.sleep(1/30.0)


if inputSelection == 1:
    while True:
        for frame in buf:
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                camera.schedule_frame(rgb)
                time.sleep(1/10.0)
#while True:
#
#    if inputSelection == 0:
#        ret, frame = cameraCap.read()
#        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#        camera.schedule_frame(rgb)
#        time.sleep(1/30.0)
#
#    if inputSelection == 1:
#        for frame in buf:
#                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                camera.schedule_frame(rgb)
#                time.sleep(1/15.0)
