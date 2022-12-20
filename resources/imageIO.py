import cv2
import numpy
import glob

import fileIO

###############################################################################
def imgIO_saveImageSequence(gImgStack, path):
    try:
        fileIO.fileIO_writeToLog("imgIO_saveImageSequence. Saving image sequence to directory %s." %(path), True)
        [row, col, numFrames] = gImgStack.shape
        for frame in range(numFrames):
            fileName = path + "/" + str(frame + 1).zfill(6) + ".png"
            cv2.imwrite(fileName, gImgStack[:, :, frame])
            
    except:
        fileIO.fileIO_writeToLog("ERROR. saveImageSequence. Unable to write image stack to %s" %(path), True)
###############################################################################

###############################################################################
def imgIO_loadImageSequence(path, extension):
    pattern = path + "/*." + extension
    filesWithPath = glob.glob(pattern)
    filesWithPath.sort()
    
    gImg = cv2.imread(filesWithPath[0], -1)
    [row, col] = gImg.shape
    numFrames = len(filesWithPath)
    gImgStack = numpy.zeros([row, col, numFrames], dtype = gImg.dtype)
    
    for frame in range(numFrames):
        gImg = cv2.imread(filesWithPath[frame], -1)
        gImgStack[:, :, frame] = gImg
        
    return gImgStack
###############################################################################