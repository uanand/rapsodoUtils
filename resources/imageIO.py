import cv2

def imgIO_saveImageSequence(gImgStack, path):
    try:
        [row, col, numFrames] = gImgStack.shape
        for frame in range(numFrames):
            fileName = path + "/" + str(frame + 1).zfill(6) + ".png"
            cv2.imwrite(fileName, gImgStack[:, :, frame])
            
    except:
        print("ERROR. saveImageSequence. Unable to write image stack to %s" %(path))
        