import os
import sys
import numpy
import matplotlib.pyplot as plt

plt.style.use("uanand")

sys.path.append(os.path.abspath('../resources'))

import imageIO

inputDir = r"C:\Users\utkarsh\Desktop\images"
exposureList = range(1, 501, 10)
minExposure, maxExposure = 0, 500

gImgStack = imageIO.imgIO_loadImageSequence(inputDir, "tif")
[row, col, numFrames] = gImgStack.shape

meanIntensity = []
for frame in range(numFrames):
    gImg = gImgStack[:, :, frame]
    meanIntensity.append(numpy.mean(gImg))
    
fig = plt.figure(figsize = (3, 2))
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(exposureList, meanIntensity)
ax.set_xlabel("Exposure key")
ax.set_ylabel("Intensity (a.u.)")
ax.set_xlim(minExposure, maxExposure)
ax.set_ylim(0, 65535)
plt.savefig("AverageIntensityPlot.png", format = "png")
plt.show()

fout = open("meanIntensity.txt", "w")
fout.write("Exposure\tImage average intensity\n")
for exp, val in zip(exposureList, meanIntensity):
    fout.write("%d\t%.6f\n" %(exp, val))
fout.close()