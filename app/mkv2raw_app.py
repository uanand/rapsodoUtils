import os
import sys

sys.path.append(os.path.abspath('../resources'))

import imageConvert

inputFile = sys.argv[1]
message = imageConvert.mkv2raw(inputFile)
print (message)
