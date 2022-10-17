import os
import sys

sys.path.append(os.path.abspath('../resources'))

import imageConvert

riffile = sys.argv[1]
spinMkvFile = riffile + "/spin_server.mkv"
spinRawFile = riffile + "/spin_server.raw"

imageConvert.mkv2raw(spinMkvFile)
os.system("../external/splitSpinCamRaw %s" %(spinRawFile))