minExposure = 1
maxExposure = 26

minGain = 0
maxGain = 23

resolutionList = [[640, 480]]

imgDir    = "/data/exposureTest"
binDir    = "/rapsodo/rapsodo_test"
scriptDir = "/rapsodo/utils"
binName   = "./rapsodo_gscamera_test.bin"

f = open("imageSeries.sh", "w")

f.write("cd %s\n" %(binDir))
f.write("mkdir %s\n" %(imgDir))

for resolution in resolutionList:
    width, height = resolution[0], resolution[1]
    for exposure in range(minExposure, maxExposure + 1):
        for gain in range(minGain, maxGain + 1):
            captureImgcommand = "%s -w %d -h %d -e %d -g %d -c 1 -l 0 -o %s" %(binName, width, height, exposure, gain, imgDir)
            currentFileName   = "%s/frame_0_exp_%d_gain_%d.png" %(imgDir, exposure, gain)
            newFileName       = imgDir + "/width_" + str(width).zfill(4) + "_height_" + str(height).zfill(4) + "_exp_" + str(exposure).zfill(2) + "_gain_" + str(gain).zfill(2) + ".png"
            "%s/width_%4d_height_%4d_exp_%2d_gain_%2d.png" %(imgDir, width, height, exposure, gain)
            renameCommand     = "mv %s %s" %(currentFileName, newFileName)
            
            f.write("%s\n" %(captureImgcommand))
            f.write("%s\n" %(renameCommand))
            
f.write("cd %s\n" %(scriptDir))
f.close()