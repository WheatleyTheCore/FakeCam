#!/usr/bin/env python3

import cv2
import numpy as np

from getFrame import *
from processImage import *

cap = cv2.VideoCapture(0)

while True:
    rawFrame = getCameraFrame(cap)
    processedFrame = processImage(rawFrame)

    print(processedFrame.shape)
