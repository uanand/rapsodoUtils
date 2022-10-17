import os

def mkv2raw(fileName):
    mkvName = fileName.split("/")[-1]
    dirName = fileName.split(mkvName)[0]
    rawName = dirName + mkvName.replace(".mkv", ".raw")
    
    print ("Converting %s to %s" %(fileName, rawName))
    
    try:
        os.system("gst-launch-1.0 filesrc location=%s ! matroskademux name=demux ! queue ! h265parse ! avdec_h265 ! videoconvert ! video/x-raw, format=GRAY16_LE ! filesink location=%s" %(fileName, rawName))
        message = "Conversion successful"
    except:
        message = "Conversion failed"
        
    return message
    
