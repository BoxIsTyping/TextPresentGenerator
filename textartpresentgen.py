import random

def generatePresent(height = 5, width = 20, ribbonSize = 4, bowSize = 2):
    #Reate empty string called "present"; 
    present = "" #Will store the finished ascii art and be returned
    
    ##input fixing
    if(ribbonSize < 3):
        ribbonSize = 3
    if (width < height):
        height = 5
        width = 20


    #define present materials
    baseMats = ["X", "0", "#", "O", "&", "@", "$", "8"]
    hRibbonMats = ["~", "=", "-"]
    vRibbonMats = ["I", "|", "!", ";", ":"]
    bowLeftMats = ["\\", "[", ")", ">"]
    bowRightMats = ["/", "]", "(", "<"]

    #Pick mats for present
    baseMat = random.choice(baseMats)
    hRibbonMat = random.choice(hRibbonMats)
    vRibbonMat = random.choice(vRibbonMats)
    bowMatNumber = random.randint(0, 3)
    bowLeftMat = bowLeftMats[bowMatNumber]
    bowRightMat = bowRightMats[bowMatNumber]

    vRibbonSize = ribbonSize
    hRibbonSize = int(ribbonSize/3)

    #Create presnet by appending characters to "present" string
    #First add all items in row, then meve to next col

    #Create vertical ribbon starting point
    vRibbonStart = random.randint(2, width - vRibbonSize - 2)
    vRibbonEnd = vRibbonStart + vRibbonSize
    #Create horizontal ribbon starting point
    hRibbonStart = random.randint(1, height - hRibbonSize - 2)
    hRibbonEnd = hRibbonStart + hRibbonSize



    #Create bow
    for i in range(0, bowSize):
        
        for j in range (0, width + 1):
            if(j >= vRibbonStart - bowSize - 1 and j < vRibbonStart + vRibbonSize/2): #Cursor less than ribbon + offset and not in center
                present += bowLeftMat
            elif(j <= vRibbonEnd + bowSize + 1 and j > vRibbonStart + vRibbonSize/2): #cursor at 2nd half of bow
                present += bowRightMat
            else: #not at bow tile/ add filler space to even out lines
                present += " "
        
        #move cursor to next line
        present += "\n"


    #Create Main Present
    for i in range(0, height):

        for j in range(0, width): #Place next tile in horizontal row
            if(i >= hRibbonStart and i <= hRibbonEnd): #If in h ribbon section
                present += hRibbonMat
            elif(j >= vRibbonStart and j <= vRibbonEnd): #if in V ribbon section
                present += vRibbonMat
            elif((i < hRibbonStart or i > hRibbonStart) and (j < vRibbonStart or j > vRibbonEnd)): #if cursor is not in ribbon section
                present += baseMat
                

        present += "\n"
    return present


#make up some values for testing
width = random.randint(15, 100)
height = int(width/random.randint(3, 6))
ribbonSize = int(width/random.randint(4, 7))
bowSize = int(ribbonSize/2)


#display result of generator
print(generatePresent(height, width, ribbonSize, bowSize))



