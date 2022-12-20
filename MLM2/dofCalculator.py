import os
import sys

sys.path.append(os.path.abspath('../resources'))

import convertUnit

def selectCamera(type):
    if (type == "pitching"):
        pixelSize_um   = 4.4
        numPixelX      = 640
        numPixelY      = 512
        focalLength_mm = 8
        fNumber        = 2.8
        nearDOF_m      = 1
        farDOF_m       = 15
        coc_pixels     = 0.5
    elif (type == "hitting"):
        pixelSize_um   = 4.4
        numPixelX      = 640
        numPixelY      = 512
        focalLength_mm = 4
        fNumber        = 2.8
        nearDOF_m      = 0.5
        farDOF_m       = 10
        coc_pixels     = 0.5
        
    pixelSize   = convertUnit.cnvt_um2m(pixelSize_um)
    focalLength = convertUnit.cnvt_mm2m(focalLength_mm)
    nearDOF     = nearDOF_m
    farDOF      = farDOF_m
    coc         = coc_pixels
    
    return pixelSize, numPixelX, numPixelY, focalLength, fNumber, nearDOF, farDOF, coc
    
def estimateDOF(pixelSize, focalLength, fNumber, coc, focusDistance):
    H     = focalLength**2 / (fNumber * pixelSize * coc)
    DOF_N = H * focusDistance / (H + focusDistance)
    DOF_F = H * focusDistance / (H - focusDistance)
    DOF   = DOF_F - DOF_N
    # DOF   = 2 * H * focusDistance * (focusDistance - focalLength) / (H**2 - (focusDistance - focalLength)**2)
    
    if (DOF_F < 0):
        DOF_F = float('inf')
        DOF   = float('inf')
            
    return DOF_N, DOF_F, DOF

def main(type):
    outFile = open("dofCalculator_%s.txt" %(type), "w")
    outFile.write("Camera type\tFocal length (m)\tFocus distance (m)\tCircle of confusion (num pixels)\tDOF_N (m)\tDOF_F (m)\tDOF (m)\tStatus\n")
    
    pixelSize, numPixelX, numPixelY, focalLength, fNumber, nearDOF, farDOF, coc = selectCamera(type)
    
    focusDistanceList = range(1, 21)
    for focusDistance in focusDistanceList:
        DOF_N, DOF_F, DOF = estimateDOF(pixelSize, focalLength, fNumber, coc, focusDistance)
        
        if (DOF_N <= nearDOF and DOF_F >= farDOF):
                status = "Good"
            else:
                status = "Bad"
            outFile.write("%s\t%.6f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%s\n" %(type, focalLength, focusDistance, coc, DOF_N, DOF_F, DOF, status))
    outFile.close()
    
main(sys.argv[1])

