#!/usr/bin/env python3

import numpy as np
import cv2

def getCameraFrame(cap):
    ret, frame = cap.read()
    rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return rgbFrame
