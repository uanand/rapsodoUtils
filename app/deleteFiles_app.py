import os
import sys
import platform

sys.path.append(os.path.abspath('../resources'))

import fileIO

rifFile = sys.argv[1]

deleteFileList = ["cam-0-mkv.raw", "cam-1-mkv.raw", "ingame.mkv_2.raw", "spin_server.raw", "spin_client.raw", "speed_server.raw", "speed_client.raw"]

for deleteFile in deleteFileList:
    fileIO.fileIO_rmFile(rifFile + "/" + deleteFile)
    