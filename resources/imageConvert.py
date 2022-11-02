import os
import numpy
import imageio
import imutils
import cv2

###############################################################################
def mkv2raw(fileName):
    mkvName = fileName.split("/")[-1]
    dirName = fileName.split(mkvName)[0]
    rawName = dirName + mkvName.replace(".mkv", ".raw")
    
    print ("Converting %s to %s" %(fileName, rawName))
    
    try:
        os.system("gst-launch-1.0 filesrc location=%s ! matroskademux name=demux ! queue ! h265parse ! avdec_h265 ! videoconvert ! video/x-raw, format=GRAY16_LE ! filesink location=%s" %(fileName, rawName))
        message = "Conversion successful"
    except:
        message = "Conversion failed"
        
    return message
###############################################################################

###############################################################################
def movie2stack(fileName, mode = "grayscale"):
    try:
        print("movie2stack. Loading movie %s to 3D stack" %(fileName))
        reader = imageio.get_reader(fileName)
        
        col,row = reader.get_meta_data()['size']
        numFrames = reader.count_frames()
        
        if (mode == "grayscale"):
            gImgStack = numpy.zeros([row, col, numFrames], dtype= "uint8")
            
        for frame in range(numFrames):
            img = reader.get_data(frame)
            if (mode == "grayscale"):
                img = rgb2gray(img)
                gImgStack[:, :, frame] = img
                
        reader.close()
        
        return gImgStack
    except:
        print('ERROR. movie2stack. File corrupt or format not supported.' %(fileName))
###############################################################################

###############################################################################
def rgb2gray(img):
    gImg = numpy.mean(img, axis = 2).astype("uint8")
    return gImg
###############################################################################

###############################################################################
def gray2rgb(gImg):
    [row, col] = gImg.shape
    rgbImg = numpy.zeros([row, col, 3], dtype = "uint8")
    
    rgbImg[:, :, 0] = gImg
    rgbImg[:, :, 1] = gImg
    rgbImg[:, :, 2] = gImg
    
    return rgbImg
###############################################################################

###############################################################################
def imageStackResize(gImgStack, scale):
    try:
        print ("Rescaling the image stack.")
        [row, col, numFrames] = gImgStack.shape
        row_scale, col_scale = int(numpy.round(row * scale)), int(numpy.round(col * scale))
        gImgStackResize = numpy.zeros([row_scale, col_scale, numFrames], dtype = "uint8")
        
        for frame in range(numFrames):
            gImg = gImgStack[:, :, frame]
            gImg = cv2.resize(gImg,(col_scale, row_scale), interpolation = cv2.INTER_AREA)
            
            gImgStackResize[:, :, frame] = gImg
            
        return gImgStackResize
    except:
        print("Cannot resize the image stack.")
###############################################################################

###############################################################################
def imgStackRotate(gImgStack, angle):
    try:
        print ("imgStackRotate. Rotating the image stack by %.2f degrees." %(angle))
        [row, col, numFrames] = gImgStack.shape
        gImgStackRot = numpy.zeros([row, col, numFrames], dtype = "uint8")
        
        for frame in range(numFrames):
            gImg = gImgStack[:, :, frame]
            gImgRot = imutils.rotate(gImg, angle)
            
            gImgStackRot[:, :, frame] = gImgRot
            
        return gImgStackRot
    except:
        print("ERROR: imgStackRotate. Unable to rotate image stack by %.2f degrees." %(angle))
###############################################################################