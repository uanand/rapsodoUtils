import os
import shutil
import timeUtils
import platform

###############################################################################
def fileIO_mkdir(dirName):
    try:
        os.mkdir(dirName)
    except:
        fileIO_writeToLog("WARNING: fileIO_mkdir. Unable to create directory %s." %(dirName), True)
###############################################################################

###############################################################################
def fileIO_dirExists(dirName):
    try:
        if (os.path.exists(dirName)):
            return True
        else:
            fileIO_writeToLog("WARNING: fileIO_dirExists. Directory %s does not exist." %(dirName))
            return False
    except:
        fileIO_writeToLog("ERROR: fileIO_dirExists. Unable to check if directory %s exists." %(dirName), True)
###############################################################################

###############################################################################
def fileIO_clearDir(dirName, fileTypes):
    try:
        for root, dirs, files in os.walk(dirName):
            for name in files:
                for fileType in fileTypes:
                    if (fileType in name):
                        fileName = os.path.join(root, name)
                        fileIO_rmFile(fileName)
    except:
        fileIO_writeToLog("ERROR: fileIO_clearDir. Unable to remove files from directory %s." %(dirName), True)
###############################################################################

###############################################################################
def fileIO_rmFile(fileName):
    try:
        if (fileIO_fileExists(fileName) == True):
            os.remove(fileName)
        else:
            fileIO_writeToLog("WARNING: fileIO_rmFile. %s does not exist" %(fileName))
    except:
        fileIO_writeToLog("ERROR: fileIO_rmFile. Unable to remove %s." %(fileName), True)
###############################################################################

###############################################################################
def fileIO_fileExists(fileName):
    try:
        if (os.path.isfile(fileName)):
            return True
        else:
            fileIO_writeToLog("WARNING: fileIO_fileExists. File %s does not exist." %(fileName))
            return False
    except:
        fileIO_writeToLog("ERROR: fileIO_fileExists. Unable to check if file %s exists." %(fileName), True)
###############################################################################

###############################################################################
def fileIO_mvDir(sourceDir, destDir, fileTypes):
    try:
        for root, dirs, files in os.walk(sourceDir):
            for name in files:
                for fileType in fileTypes:
                    if (fileType in name):
                        sourceFileName = os.path.join(root, name)
                        destFileName   = destDir + "/" + name
                        fileIO_mvFile(sourceFileName, destFileName)
    except:
        fileIO_writeToLog("ERROR: fileIO_mvDir. Unable to move files from %s to %s." %(sourceDir, destDir), True)
###############################################################################

###############################################################################
def fileIO_mvFile(source, destination):
    try:
        if (fileIO_fileExists(destination) == True):
            fileIO_writeToLog("WARNING: fileIO_mvFile. %s already exists. Deleting it." %(destination))
            fileIO_rmFile(destination)
        if (fileIO_fileExists(source) == True):
            shutil.copy(source, destination)
        else:
            fileIO_writeToLog("WARNING: fileIO_mvFile. %s does not exist." %(source))
    except:
        fileIO_writeToLog("ERROR: fileIO_mvFile. Unable to move %s to %s." %(source, destination), True)
###############################################################################

###############################################################################
def fileIO_findSubDir(dirName, recursive = False):
    try:
        if (recursive == False):
            subDirList = []
            for iter in os.scandir(dirName):
                if (iter.is_dir()):
                    subDirList.append(iter.path)
            return subDirList
    except:
        fileIO_writeToLog("ERROR: fileIO_findSubDir. Unable to find subdirectories inside %s." %(dirName), True)
###############################################################################

###############################################################################
def fileIO_writeToLog(message, printFlag = False):
    try:
        f = open("../log/process.log", "a+")
        timeStamp = timeUtils.timeUtils_timestamp()
        f.write("%s\t%s\n" %(timeStamp, message))
        f.close()
        
        if (printFlag == True):
            print(message)
    except:
        print("ERROR: Unable to open log file.")
###############################################################################

###############################################################################
def fileIO_selectFilesInDir(dirName, contents):
    try:
        fileNameList = []
        for root, dirs, files in os.walk(dirName):
            for name in files:
                for content in contents:
                    if (content in name):
                        fileName  = os.path.join(root, name)
                        fileNameList.append(fileName)
                        
        return fileNameList
    except:
        fileIO_writeToLog("ERROR: fileIO_selectFilesInDir. %s failed." %(dirName), True)
        return None
###############################################################################

###############################################################################
def fileIO_getFileName(fileNameWithPath):
    try:
        if (platform.system() == "Linux"):
            fileName = fileNameWithPath.split("/")[-1]
        elif (platform.system() == "Windows"):
            fileName = fileNameWithPath.split("\\")[-1]
            
        return fileName
    except:
        fileIO_writeToLog("ERROR: fileIO_getFileName. Unable to get file namee for %s." %(fileNameWithPath), True)
###############################################################################