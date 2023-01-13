import os
import sys
import platform

sys.path.append(os.path.abspath('../resources'))

import fileIO

rifFile = sys.argv[1]

deleteFileList = ["cam-0-mkv.raw", "cam-1-mkv.raw", "ingame.mkv_2.raw"]

if (platform.system() == "Windows"):
    rifFileName          = rifFile.split("\\")[-1]
else:
    rifFileName          = rifFile.split("/")[-1]
    
if ("_server" in rifFileName):
    riffTimeStamp = rifFileName.split("_server")[0]
elif ("_client" in rifFileName):
    riffTimeStamp = rifFileName.split("_client")[0]
    
for deleteFile in deleteFileList:
    fileIO.fileIO_rmFile(rifFile + "/" + deleteFile)
    