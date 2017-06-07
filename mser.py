import os
import sys
import cv2
import numpy as np

from PIL import Image

"""
    This is a simple example on how to use OpenCV for MSER
"""

def mser(cv_image):
    vis = cv_image.copy()
    mser = cv2.MSER_create()
    regions, _ = mser.detectRegions(cv_image)
    for p in regions:
        xmax, ymax = np.amax(p, axis=0)
        xmin, ymin = np.amin(p, axis=0)
        cv2.rectangle(vis, (xmin,ymax), (xmax,ymin), (0, 255, 0), 1)
    return vis

def main(argv):
    file_path = argv[1]
    save_path = argv[2]

    cv2.imwrite(save_path, mser(cv2.imread(file_path, 0)))

if __name__=='__main__':
    main(sys.argv)