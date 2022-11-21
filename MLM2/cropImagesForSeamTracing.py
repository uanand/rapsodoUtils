import os
import sys
import numpy
import cv2
from skimage.transform import resize
from tqdm import tqdm

sys.path.append(os.path.abspath('../resources'))

import fileIO
import imageConvert

rescaledSize = 80
cropList = [\
    [368, 182, 23, 22],\
    [322, 323, 28, 29],\
    [277, 105, 40, 40],\
    [544, 397, 45, 47],\
    [246, 226, 65, 66]\
]
    
inputDir  = sys.argv[1]
outputDir = sys.argv[2]

fileIO.fileIO_mkdir(outputDir)
for i in range(len(cropList)):
    fileIO.fileIO_mkdir(outputDir + "/crop_" + str(i+1))
    
fileNameList = fileIO.fileIO_selectFilesInDir(inputDir, [".png"])
for fileNameWithPath in tqdm(fileNameList):
    fileName = fileIO.fileIO_getFileName(fileNameWithPath)
    gImg = cv2.imread(fileNameWithPath, -1)
    for i in range(len(cropList)):
        crop = cropList[i]
        startRow, startCol, height, width = crop[1], crop[0], crop[3], crop[2]
        gImgCrop = gImg[startRow:startRow + height, startCol:startCol + width]
        gImgCropResize = resize(gImgCrop, (rescaledSize, rescaledSize))
        gImgCropResize = imageConvert.imgCnvt_normalize(gImgCropResize)
        cv2.imwrite(outputDir + "/crop_" + str(i+1) + "/" + fileName, gImgCropResize)