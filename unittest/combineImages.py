import os
import sys
import cv2
import glob
import numpy

inputDir = sys.argv[1]

fileNameList = glob.glob(inputDir + "/" + "*.png")
fileNameList.sort()

for fileName in fileNameList:
    gImg = cv2.imread(fileName, 0)
    try:
        gImgCombined = numpy.vstack((gImgCombined, gImg))
    except:
        gImgCombined = gImg.copy()
        
cv2.imwrite("combined.png", gImgCombined)