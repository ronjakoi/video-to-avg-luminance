#!/usr/bin/env python3

"""
This script calculates the mean relative luminance for every frame
of a video file. It prints a floating point value for one frame per line.

Ronja Koistinen <ronja@tuxera.com>
"""

# pylint: disable=c-extension-no-member
# pylint: disable=missing-function-docstring

import argparse
import sys
import cv2 as cv

def main():
    parser = argparse.ArgumentParser(
        description=__doc__
    )

    parser.add_argument('video', type=str, help='Path to video file')
    args = parser.parse_args()

    cap = cv.VideoCapture(args.video)

    frames_read = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            if frames_read == 0:
                print("Zero frames read! Is this file broken?", file=sys.stderr)
            break
        frames_read += 1

        # there is also cv.COLOR_RGB2GRAY which possibly does the same thing,
        # but it's difficult to tell from the documentation
        lab = cv.cvtColor(frame, cv.COLOR_RGB2LAB)
        luminance, _, _ = cv.split(lab)

        print(luminance.mean())

if __name__ == "__main__":
    main()
