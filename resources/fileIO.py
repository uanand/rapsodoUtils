import os
import shutil

###############################################################################
def fileIO_mkdir(dirName):
    try:
        if (fileIO_dirExists(dirName) == True):
            print("WARNING. fileIO_mkdir. Directory %s already exists" %(dirName))
        else:
            os.mkdir(dirName)
    except:
        print("ERROR: fileIO_mkdir. Unable to create directory %s." %(dirName))
###############################################################################

###############################################################################
def fileIO_dirExists(dirName):
    try:
        if (os.path.exists(dirName)):
            return True
        else:
            print("WARNING: fileIO_dirExists. Directory %s does not exist." %(dirName))
            return False
    except:
        print("ERROR: fileIO_dirExists. Unable to check if directory %s exists." %(dirName))
###############################################################################

###############################################################################
def fileIO_clearDir(dirName, fileTypes):
    try:
        print("fileIO_clearDir. Removing files from directory %s." %(dirName))
        for root, dirs, files in os.walk(dirName):
            for name in files:
                for fileType in fileTypes:
                    if (fileType in name):
                        fileName = os.path.join(root, name)
                        fileIO_rmFile(fileName)
    except:
        print("ERROR: fileIO_clearDir. Unable to remove files from directory %s." %(dirName))
###############################################################################

###############################################################################
def fileIO_rmFile(fileName):
    try:
        if (fileIO_fileExists(fileName) == True):
            os.remove(fileName)
        else:
            print("WARNING: fileIO_rmFile. %s does not exist" %(fileName))
    except:
        print("ERROR: fileIO_rmFile. Unable to remove %s." %(fileName))
###############################################################################

###############################################################################
def fileIO_fileExists(fileName):
    try:
        if (os.path.isfile(fileName)):
            return True
        else:
            print("WARNING: fileIO_fileExists. File %s does not exist." %(fileName))
            return False
    except:
        print("ERROR: fileIO_fileExists. Unable to check if file %s exists." %(fileName))
###############################################################################

###############################################################################
def fileIO_mvDir(sourceDir, destDir, fileTypes):
    try:
        print("fileIO_mvDir. Moving files from %s to %s." %(sourceDir, destDir))
        for root, dirs, files in os.walk(sourceDir):
            for name in files:
                for fileType in fileTypes:
                    if (fileType in name):
                        sourceFileName = os.path.join(root, name)
                        destFileName   = destDir + "/" + name
                        fileIO_mvFile(sourceFileName, destFileName)
    except:
        print("ERROR: fileIO_mvDir. Unable to move files from %s to %s." %(sourceDir, destDir))
###############################################################################

###############################################################################
def fileIO_mvFile(source, destination):
    try:
        if (fileIO_fileExists(destination) == True):
            print("WARNING: fileIO_mvFile. %s already exists. Deleting it." %(destination))
            fileIO_rmFile(destination)
        if (fileIO_fileExists(source) == True):
            shutil.copy(source, destination)
            # os.rename(source, destination)
        else:
            print("WARNING: fileIO_mvFile. %s does not exist." %(source))
    except:
        print("ERROR: fileIO_mvFile. Unable to move %s to %s." %(source, destination))
###############################################################################