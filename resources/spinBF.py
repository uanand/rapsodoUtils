import cv2
import numpy
from scipy import ndimage

import imageConvert
import fileIO

def spinBF_consoleImage(imgDir, imgStack, consoleImgPath):
    try:
        scale = 4
        [row, col, numFrames] = imgStack.shape
        consoleImg = imgStack[:, :, 0]
        consoleImgBGR = imageConvert.imgCnvt_gray2rgb(consoleImg)
        
        for frame in range(numFrames):
            bgrImg = cv2.imread(imgDir + "/" + str(frame + 1).zfill(6) + ".png")
            gImgFull = imgStack[:, :, frame]
            
            red0 = bgrImg[:, :, 0] == 0
            red1 = bgrImg[:, :, 1] == 0
            red2 = bgrImg[:, :, 2] == 255
            red = numpy.logical_and(red0, numpy.logical_and(red1, red2))
            
            if (numpy.max(red) == True):
                labelImg, numLabels = ndimage.label(red, structure = [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
                
                for labelN in range(1, numLabels + 1):
                    redLabel = labelImg==labelN
                    [r, c] = numpy.where(redLabel == True)
                    
                    rMin, rMax = numpy.min(r), numpy.max(r)
                    cMin, cMax = numpy.min(c), numpy.max(c)
                    
                    rMin, rMax = rMin * scale, rMax * scale
                    cMin, cMax = cMin * scale, cMax * scale
                    
                    consoleImgBGR[rMin : rMax + 1, cMin : cMax + 1, 0] = gImgFull[rMin : rMax + 1, cMin : cMax + 1]
                    consoleImgBGR[rMin : rMax + 1, cMin : cMax + 1, 1] = gImgFull[rMin : rMax + 1, cMin : cMax + 1]
                    consoleImgBGR[rMin : rMax + 1, cMin : cMax + 1, 2] = gImgFull[rMin : rMax + 1, cMin : cMax + 1]
                    
                    consoleImgBGR = cv2.rectangle(consoleImgBGR, (cMin, rMin), (cMax, rMax), (0, 0, 255), 1)
                
        cv2.imwrite(consoleImgPath, consoleImgBGR)
    except:
        fileIO.fileIO_writeToLog("ERROR: spinBF_consoleImage. Unable to create spin ball finding console image %s." %(consoleImgPath), True)