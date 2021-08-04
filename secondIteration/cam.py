#!/usr/bin/env python3

import pyvirtualcam
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

with pyvirtualcam.Camera(width=640, height=480, fps=20) as cam:
    print(f'Using virtual camera: {cam.device}')
    while True:
        ret, rawFrame = cap.read()  #BGR
        frame = cv2.cvtColor(rawFrame, cv2.COLOR_BGR2RGB) #convert to rgb
        cam.send(frame)
        cam.sleep_until_next_frame()
