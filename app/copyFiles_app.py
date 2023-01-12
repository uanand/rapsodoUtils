import os
import sys
import platform

sys.path.append(os.path.abspath('../resources'))

import fileIO

rifFile = sys.argv[1]

fileContainsList = [".mkv"]
dataDir = "../output"
fileIO.fileIO_mkdir(dataDir)

if (platform.system() == "Windows"):
    rifFileName          = rifFile.split("\\")[-1]
else:
    rifFileName          = rifFile.split("/")[-1]
    
if ("_server" in rifFileName):
    riffTimeStamp = rifFileName.split("_server")[0]
elif ("_client" in rifFileName):
    riffTimeStamp = rifFileName.split("_client")[0]
    
outputDir = dataDir + "/" + riffTimeStamp
fileIO.fileIO_mkdir(outputDir)

sourceFileList = fileIO.fileIO_selectFilesInDir(rifFile, fileContainsList)
for sourceFile in sourceFileList:
    fileName = fileIO.fileIO_getFileName(sourceFile)
    fileIO.fileIO_cpFile(sourceFile, outputDir + "/" + fileName)
    
