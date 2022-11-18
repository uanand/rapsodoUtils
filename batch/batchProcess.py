import os
import sys

sys.path.append(os.path.abspath('../resources'))

import fileIO

pythonExecutable = "python3"
pythonScript = sys.argv[1]
dataDir = sys.argv[2]

f = open("batchProcess.sh", "w")
f.write("#!/bin/bash\n")
f.write('export LD_LIBRARY_PATH=":./:/rap_fs/lib/libtvm/:/rap_fs/lib/apriltag:/rap_fs/lib/tkdnn_lib:/rap_fs/lib/libne10:/rap_fs/lib/libgpiod:/rap_fs/lib/libtvm/:/rap_fs/lib/sloglib/:/rap_fs/lib/rdevicelib/:/rap_fs/lib/seam/"\n')
f.write("cd ../app\n")

subDirList = fileIO.fileIO_findSubDir(dataDir)
for subDir in subDirList:
    f.write("%s %s \"%s\"\n" %(pythonExecutable, pythonScript, subDir))
    
f.write("cd ../batch\n")
f.close()

os.system("bash batchProcess.sh")
