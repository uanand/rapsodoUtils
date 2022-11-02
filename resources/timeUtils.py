import os
import sys
import datetime

import fileIO

############################################################
def timeUtils_timestamp(delimiter = "\t"):
    try:
        if (delimiter == "\t"):
            string = datetime.datetime.now().strftime("%Y%m%d\t%H%M%S")
        elif (delimiter == "_"):
            string = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        elif (delimiter == " "):
            string = datetime.datetime.now().strftime("%Y%m%d %H%M%S")
        elif (delimiter == ":"):
            string = datetime.datetime.now().strftime("%Y%m%d:%H%M%S")
        elif (delimiter == ","):
            string = datetime.datetime.now().strftime("%Y%m%d,%H%M%S")
        elif (delimiter == "."):
            string = datetime.datetime.now().strftime("%Y%m%d.%H%M%S")
        else:
            string = datetime.datetime.now().strftime("%Y%m%d\t%H%M%S")
        return string
    except:
        fileIO.fileIO_writeToLog("ERROR: Unable to get time stamp. Return 00000000\t000000.", True)
        string = "00000000\t000000"
        return string
############################################################