import os
import sys
import platform

sys.path.append(os.path.abspath('../resources'))

import imageConvert
import imageIO
import fileIO
import spinBF

crop_row, crop_col, crop_height, crop_width = 0, 400, 2048, 2048
imagePath = "../external/ingame_bf_api/data/imx250"
bfProcessedImagePath = "../external/ingame_bf_api/bin"
normalizeFlag = False
rifFile = sys.argv[1]

if (platform.system() == "Windows"):
    rifFileName          = rifFile.split("\\")[-1]
else:
    rifFileName          = rifFile.split("/")[-1]
    
rifResultDir            = rifFile + "/result"
rifResultImagePath      = rifResultDir + "/spinBallFinding"
rifResultConsolePath    = rifResultDir + "/spinBallFindingConsole.png"

logDir = "../log"
fileIO.fileIO_mkdir(logDir)

continueFlag = True
if ("_server" in rifFile):
    inputFile = rifFile + "/spin_server.mkv"
elif ("_client" in rifFile):
    inputFile = rifFile + "/spin_client.mkv"
else:
    fileIO.fileIO_writeToLog("ERROR: Incorrect RIF file %s. Try again." %(rifFile), True)
    continueFlag = False
    
if (continueFlag == True):
    fileIO.fileIO_mkdir(rifResultDir)
    fileIO.fileIO_mkdir(rifResultImagePath)
    
    fileIO.fileIO_clearDir(imagePath, fileTypes = [".png"])
    fileIO.fileIO_clearDir(bfProcessedImagePath, fileTypes = [".png"])
    
    gImgStack = imageConvert.imgCnvt_movie2stack(inputFile)
    gImgStackCrop = gImgStack[crop_row : crop_row + crop_height, crop_col : crop_col + crop_width, :]
    
    if ("_server" in inputFile):
        pass
    elif ("_client" in inputFile):
        gImgStackCrop = imageConvert.imgCnvt_imgStackRotate(gImgStackCrop, angle = 180)
        
    gImgStackScale = imageConvert.imgCnvt_imageStackResize(gImgStackCrop, 0.25)
    
    if (normalizeFlag == True):
        gImgStackScale = imageConvert.imgCnvt_imgStackNormalize(gImgStackScale)
        
    imageIO.imgIO_saveImageSequence(gImgStackScale, imagePath)
    
    os.chdir("../external/ingame_bf_api/bin")
    os.system("./test_bulk")
    os.chdir("../../../app")
    
    fileIO.fileIO_mvDir(bfProcessedImagePath, rifResultImagePath, fileTypes = [".png"])
    
    fileIO.fileIO_clearDir(imagePath, fileTypes = [".png"])
    fileIO.fileIO_clearDir(bfProcessedImagePath, fileTypes = [".png"])
    
    spinBF.spinBF_consoleImage(rifResultImagePath, gImgStackCrop, rifResultConsolePath)