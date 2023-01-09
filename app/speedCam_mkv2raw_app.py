import os
import sys

sys.path.append(os.path.abspath('../resources'))

import imageConvert

rifFile = sys.argv[1]
if ("_server" in rifFile):
    inputFile = rifFile +"/speed_server.mkv"
elif ("_client" in rifFile):
    inputFile = rifFile +"/speed_client.mkv"
message = imageConvert.imgCnvt_mkv2raw(inputFile)
print (message)
