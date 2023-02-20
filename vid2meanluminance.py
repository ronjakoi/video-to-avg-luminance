#!/usr/bin/env python3

import numpy as np
import cv2 as cv
import argparse

parser = argparse.ArgumentParser(description='Calculates the mean relative luminance for every frame of a video')
parser.add_argument('video', type=str, help='Path to video file')
args = parser.parse_args()

cap = cv.VideoCapture(args.video)

frames_read = 0

while(True):
    ret, frame = cap.read()
    if not ret:
        if frames_read == 0:
            eprint("Zero frames read! Is this file broken?")
        break
    frames_read += 1

    # there is also cv.COLOR_RGB2GRAY which possibly does the same thing,
    # but it's difficult to tell from the documentation
    lab = cv.cvtColor(frame, cv.COLOR_RGB2LAB)
    luminance, _, _ = cv.split(lab)

    print(luminance.mean())
