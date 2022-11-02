import os
import numpy
import imageio
import imutils
import cv2

import fileIO

###############################################################################
def imgCnvt_mkv2raw(fileName):
    mkvName = fileName.split("/")[-1]
    dirName = fileName.split(mkvName)[0]
    rawName = dirName + mkvName.replace(".mkv", ".raw")
    
    fileIO.fileIO_writeToLog("mkv2raw. Converting %s to %s" %(fileName, rawName), True)
    
    try:
        os.system("gst-launch-1.0 filesrc location=%s ! matroskademux name=demux ! queue ! h265parse ! avdec_h265 ! videoconvert ! video/x-raw, format=GRAY16_LE ! filesink location=%s" %(fileName, rawName))
        message = "Conversion successful"
    except:
        message = "Conversion failed"
        
    return message
###############################################################################

###############################################################################
def imgCnvt_movie2stack(fileName, mode = "grayscale"):
    try:
        fileIO.fileIO_writeToLog("imgCnvt_movie2stack. Loading movie %s to 3D stack" %(fileName), True)
        reader = imageio.get_reader(fileName)
        
        col,row = reader.get_meta_data()['size']
        numFrames = reader.count_frames()
        
        if (mode == "grayscale"):
            gImgStack = numpy.zeros([row, col, numFrames], dtype= "uint8")
            
        for frame in range(numFrames):
            img = reader.get_data(frame)
            if (mode == "grayscale"):
                img = imgCnvt_rgb2gray(img)
                gImgStack[:, :, frame] = img
                
        reader.close()
        
        return gImgStack
    except:
        fileIO.fileIO_writeToLog("ERROR. imgCnvt_movie2stack. File %s corrupt or format not supported." %(fileName), True)
###############################################################################

###############################################################################
def imgCnvt_rgb2gray(img):
    try:
        gImg = numpy.mean(img, axis = 2).astype("uint8")
        return gImg
    except:
        fileIO.fileIO_writeToLog("ERROR: imgCnvt_rgb2gray. Failed to convert RGB image to grayscale.", True)
###############################################################################

###############################################################################
def imgCnvt_gray2rgb(gImg):
    try:
        [row, col] = gImg.shape
        rgbImg = numpy.zeros([row, col, 3], dtype = "uint8")
        
        rgbImg[:, :, 0] = gImg
        rgbImg[:, :, 1] = gImg
        rgbImg[:, :, 2] = gImg
        
        return rgbImg
    except:
        fileIO.fileIO_writeToLog("ERROR: imgCnvt_gray2rgb. Failed to convert grayscale image to RGB.", True)
###############################################################################

###############################################################################
def imgCnvt_imageStackResize(gImgStack, scale):
    try:
        fileIO.fileIO_writeToLog("imgCnvt_imageStackResize. Rescaling the image stack.", True)
        [row, col, numFrames] = gImgStack.shape
        row_scale, col_scale = int(numpy.round(row * scale)), int(numpy.round(col * scale))
        gImgStackResize = numpy.zeros([row_scale, col_scale, numFrames], dtype = "uint8")
        
        for frame in range(numFrames):
            gImg = gImgStack[:, :, frame]
            gImg = cv2.resize(gImg,(col_scale, row_scale), interpolation = cv2.INTER_AREA)
            
            gImgStackResize[:, :, frame] = gImg
            
        return gImgStackResize
    except:
        fileIO.fileIO_writeToLog("ERROR: imgCnvt_imageStackResize. Cannot resize the image stack.", True)
###############################################################################

###############################################################################
def imgCnvt_imgStackRotate(gImgStack, angle):
    try:
        fileIO.fileIO_writeToLog("imgCnvt_imgStackRotate. Rotating the image stack by %.2f degrees." %(angle), True)
        [row, col, numFrames] = gImgStack.shape
        gImgStackRot = numpy.zeros([row, col, numFrames], dtype = "uint8")
        
        for frame in range(numFrames):
            gImg = gImgStack[:, :, frame]
            gImgRot = imutils.rotate(gImg, angle)
            
            gImgStackRot[:, :, frame] = gImgRot
            
        return gImgStackRot
    except:
        fileIO.fileIO_writeToLog("ERROR: imgCnvt_imgStackRotate. Unable to rotate image stack by %.2f degrees." %(angle), True)
###############################################################################