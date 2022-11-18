import os
import sys

sys.path.append(os.path.abspath('../resources'))

import imageConvert
import fileIO

riffile = sys.argv[1]
if ("_server" in riffile):
    spinMkvFile = riffile + "/spin_server.mkv"
    spinRawFile = riffile + "/spin_server.raw"
elif ("_client" in riffile):
    spinMkvFile = riffile + "/spin_client.mkv"
    spinRawFile = riffile + "/spin_client.raw"

imageConvert.imgCnvt_mkv2raw(spinMkvFile)
os.system("../external/splitSpinCamRaw %s" %(spinRawFile))
fileIO.fileIO_rmFile(spinRawFile)