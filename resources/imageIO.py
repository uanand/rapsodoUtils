import cv2
import fileIO

def imgIO_saveImageSequence(gImgStack, path):
    try:
        fileIO.fileIO_writeToLog("imgIO_saveImageSequence. Saving image sequence to directory %s." %(path), True)
        [row, col, numFrames] = gImgStack.shape
        for frame in range(numFrames):
            fileName = path + "/" + str(frame + 1).zfill(6) + ".png"
            cv2.imwrite(fileName, gImgStack[:, :, frame])
            
    except:
        fileIO.fileIO_writeToLog("ERROR. saveImageSequence. Unable to write image stack to %s" %(path), True)
        