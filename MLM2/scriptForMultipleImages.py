import os
import sys

sys.path.append(os.path.abspath('../resources'))

import fileIO

resolutionList = [[640, 480]]
exposureList = range(1, 501, 10) # MIN, MAX = 1, 622
gainList     = [1, 5, 10, 15]       # MIN, MAX = 1, 15

imgDir    = "/data/exposureTest"
binDir    = "/rapsodo/rapsodo_test"
scriptDir = "/rapsodo/rapsodoUtils/MLM2"
binName   = "./rapsodo_gscamera_test.bin"

f = open("imageSeries.sh", "w")

f.write("cd %s\n" %(binDir))
f.write("mkdir %s\n" %(imgDir))

for resolution in resolutionList:
    width, height = resolution[0], resolution[1]
    for exposure in exposureList:
        for gain in gainList:
            captureImgcommand = "%s -w %d -h %d -e %d -g %d -c 1 -l 0 -o %s" %(binName, width, height, exposure, gain, imgDir)
            f.write("%s\n" %(captureImgcommand))
            
# for resolution in resolutionList:
#     width, height = resolution[0], resolution[1]
#     for exposure in range(minExposure, maxExposure + 1):
#         for gain in range(minGain, maxGain + 1):
#             # # currentFileName   = "%s/frame_0_exp_%d_gain_%d.png" %(imgDir, exposure, gain)
#             # currentFileName = fileIO.fileIO_selectFilesInDir(imgDir, ["frame_0_exp_%d_gain_%d_Ts_" %(exposure, gain)])[0]
#             # newFileName       = imgDir + "/width_" + str(width).zfill(4) + "_height_" + str(height).zfill(4) + "_exp_" + str(exposure).zfill(2) + "_gain_" + str(gain).zfill(2) + ".png"
#             # "%s/width_%4d_height_%4d_exp_%3d_gain_%3d.png" %(imgDir, width, height, exposure, gain)
            
#             # renameCommand     = "mv %s %s" %(currentFileName, newFileName)
            
            
#             f.write("%s\n" %(renameCommand))
            
f.write("cd %s\n" %(scriptDir))
f.close()