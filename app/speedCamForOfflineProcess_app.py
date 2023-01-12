import os
import sys

sys.path.append(os.path.abspath('../resources'))

import imageConvert
import fileIO

riffile = sys.argv[1]
speedRawFile = "ingame.mkv_2.raw"
if ("_server" in riffile):
    speedMkvFile = riffile + "/speed_server.mkv"
elif ("_client" in riffile):
    speedMkvFile = riffile + "/speed_client.mkv"
    
imageConvert.imgCnvt_mkv2raw(speedMkvFile, rawFileName = speedRawFile)