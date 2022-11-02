import cv2

def saveImageSequence(gImgStack, path):
    try:
        print("saveImageSequence. Saving image stack to path %s" %(path))
        
        [row, col, numFrames] = gImgStack.shape
        for frame in range(numFrames):
            fileName = path + "/" + str(frame + 1).zfill(6) + ".png"
            cv2.imwrite(fileName, gImgStack[:, :, frame])
            
    except:
        print("ERROR. saveImageSequence. Unable to write image stack to %s" %(path))
        