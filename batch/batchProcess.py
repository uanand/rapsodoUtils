import os
import sys
import platform
import subprocess

sys.path.append(os.path.abspath('../resources'))

import fileIO

if (platform.system() == "Windows"):
    pythonExecutable = "python"
elif (platform.system() == "Linux"):
    pythonExecutable = "python3"
    
pythonScript = sys.argv[1]
dataDir = sys.argv[2]
windowsFileName = "batchProcess.bat"
linuxFileName   = "batchProcess.sh"

if (platform.system() == "Windows"):
    f = open(windowsFileName, "w")
    f.write("cd ../app\n")
    
elif (platform.system() == "Linux"):
    f = open(linuxFileName, "w")
    f.write("#!/bin/bash\n")
    f.write('export LD_LIBRARY_PATH=":./:/rap_fs/lib/libtvm/:/rap_fs/lib/apriltag:/rap_fs/lib/tkdnn_lib:/rap_fs/lib/libne10:/rap_fs/lib/libgpiod:/rap_fs/lib/libtvm/:/rap_fs/lib/sloglib/:/rap_fs/lib/rdevicelib/:/rap_fs/lib/seam/"\n')
    f.write("cd ../app\n")
    
subDirList = fileIO.fileIO_findSubDir(dataDir)
for subDir in subDirList:
    f.write("%s %s \"%s\"\n" %(pythonExecutable, pythonScript, subDir))
    
f.write("cd ../batch\n")
f.close()

if (platform.system() == "Windows"):
    subprocess.call([windowsFileName])
    fileIO.fileIO_rmFile(windowsFileName)
elif (platform.system() == "Linux"):
    os.system("bash %s" %(linuxFileName))
    fileIO.fileIO_rmFile(linuxFileName)
