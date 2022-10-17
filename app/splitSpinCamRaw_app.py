import os
import sys
import time

inputFile = sys.argv[1]

try:
    os.system("../external/splitSpinCamRaw %s" %(inputFile))
    message = "Splitting the spin cam raw successful."
    time.sleep(2)
except:
    message = "Splitting the spin cam raw failed."
    
print (message)