# -*- coding: utf-8 -*-
"""
Created on Wed May 13 10:53:38 2020

@author: Liam
"""

class Board:
    
    def __init__(self, sideLength):
        self.sideLength=sideLength
        self.length=sideLength*sideLength
        self.array=[]
        for i in range(0,sideLength):
            for j in range(0, sideLength):
                self.array.append(0)
    
    def getCoord(self,arrayPosition):
        coords=[]
        if(arrayPosition>self.length):
            print("getCoord gives out of array exception.")
            xcoord=(None)
            ycoord=(None)
        elif(arrayPosition == 0):
            xcoord=0
            ycoord=0
        else:
            xcoord=arrayPosition%(self.sideLength)
            ycoord=int((arrayPosition-xcoord)/self.sideLength)
        coords.append(xcoord)
        coords.append(ycoord)
        return coords
    
    def getArrayPosition(self, xcoord, ycoord):
        if((xcoord>=self.sideLength)|(ycoord>self.sideLength)):
            print("getArrayPosition gives out of bound exception.")
            arrayPosition = None
        else:
            arrayPosition=(ycoord*self.sideLength)+(xcoord)
        return arrayPosition
    
    def mutilate(self, xcoord, ycoord):
        index=self.getArrayPosition(xcoord,ycoord)
        self.array[index]=1
    
    def replace(self, xcoord, ycoord):
        index=self.getArrayPosition(xcoord,ycoord)
        self.array[index]=0

    def printBoard(self):
        k=0
        for i in range(0,self.sideLength):
            row=[]
            for j in range(0,self.sideLength):
                row.append(self.array[k])
                k+=1
            print(str(row))
    
    def checkDomino1(self): # Returns True if the chessboard is sufficiently 
                            # mutilated, and returns coordinates of the first
                            # problem if it is not.
        
        indicator = False # Initialisation doesn't matter: will only get to the
                          # end if there are no squares adjacent to any other 
                          # that are both 0.
        coords=[]         
        
        for i in range(0,self.length):
            currentSquare=self.array[i]
            if(self.getCoord(i)[0] == 0):
                rightSquare=self.array[i+1]
                indicator = not((currentSquare==0) & (rightSquare==0))
                if(indicator == False):
                    coords=self.getCoord(i+1)
                    break
            elif(self.getCoord(i)[0] == (self.sideLength)-1):
                leftSquare=self.array[i-1]
                indicator = ((currentSquare == 0) & (leftSquare == 0))
                if(indicator == True):
                    coords=self.getCoord(i-1)
                    break
            else:
                rightSquare=self.array[i+1]
                leftSquare=self.array[i-1]
                indicatorLeft = ((currentSquare == 0) & (leftSquare == 0))
                indicatorRight = ((currentSquare == 0) & (rightSquare == 0) )
                indicator = not(indicatorLeft | indicatorRight)
                if(indicatorLeft == True):
                    coords=self.getCoord(i-1)
                    break
                elif(indicatorRight == True):
                    coords=self.getCoord(i+1)
                    break

            if(self.getCoord(i)[1] == 0):
                aboveSquare=self.array[i+self.sideLength]
                indicator = not((currentSquare == 0) & (aboveSquare == 0))
                if(indicator == False):
                    coords=self.getCoord(i+self.sideLength)
                    break 
            elif(self.getCoord(i)[1] == (self.sideLength-1)):
                belowSquare=self.array[i-self.sideLength]
                indicator = not((currentSquare == 0) & (belowSquare == 0))
                if(indicator == False):
                    coords=self.getCoord(i-self.sideLength)
                    break
            else:
                aboveSquare=self.array[i+(self.sideLength)]
                belowSquare=self.array[i-(self.sideLength)]
                indicatorAbove = not((currentSquare == 0) & (aboveSquare == 0) )
                indicatorBelow = not((currentSquare == 0) & (belowSquare == 0) )
                indicator = (indicatorAbove | indicatorBelow)
                if(indicatorAbove == False):
                    coords=self.getCoord(i+self.sideLength)
                    break
                elif(indicatorBelow == False):
                    coords= self.getCoord(i-self.sideLength)
                    break

        if(coords==[]):
            return indicator
        else:
            return coords
    
    def iterateMutilate(self, xCoord,yCoord):
        self.mutilate(xCoord,yCoord)
        while(self.checkDomino1()!=True):
            xcoord=self.checkDomino1()[0]
            ycoord=self.checkDomino1()[1]
            self.mutilate(xcoord,ycoord)
           
    def numberMutilate(self):
        count=0
        for elt in self.array:
            count+=elt
        return count
            
    def reset(self):
        for i in range(0,self.length):
            self.array[i]=0

    def checkDomino2(self):                 # Checks the second condition of the brief - addition of any square will allow
        indicator=True                      # a domino to be placed. Is applied after the first method, so returns true if
        for i in range(0,self.length):      # a configuration works and false if not.
            currentSquare=self.array[i]
            if(currentSquare==1):
                if(self.getCoord(i)[0]==0):
                    rightSquare=self.array[i+1]
                    if(rightSquare==1):
                        indicator = False
                        break
                elif(self.getCoord(i)[0]==(self.sideLength-1)):
                    leftSquare=self.array[i-1]
                    if(leftSquare==1):
                        indicator = False
                        break
                else:
                    rightSquare = self.array[i+1]
                    leftSquare = self.array[i-1]
                    if((rightSquare == 1)|(leftSquare == 1)):
                        indicator = False
                        break
                if(self.getCoord(i)[1]==0):
                    aboveSquare=self.array[i+self.sideLength]
                    if(aboveSquare == 1):
                        indicator = False
                        break
                elif(self.getCoord(i)[1]==self.sideLength-1):
                    belowSquare = self.array[i-self.sideLength]
                    if(belowSquare == 1):
                        indicator = False
                        break
                else:
                    aboveSquare=self.array[i+(self.sideLength)]
                    belowSquare=self.array[i-(self.sideLength)]
                    if((aboveSquare==1)|(belowSquare==1)):
                        indicator = False
                        break
        return indicator
    

def uniqueArray(array1,array2):                 # spots duplicate grids. Returns true if unique, false if not.
    indicator = True
    if(str(array1)==str(array2)):
        indicator = False
    return indicator
    
def uniqueCorrectMutilations(sideLength):      # Collects all unique correct grids and outputs them.
    boards=[]
    arrays=[]
    for i in range(0,sideLength*sideLength):
        board=Board(sideLength)
        xcoord=board.getCoord(i)[0]
        ycoord=board.getCoord(i)[1]
        board.iterateMutilate(xcoord,ycoord)
        if(board.checkDomino2()==True):
            boards.append(board)
            arrays.append(board.array)
    boardCopy=[boards[0],boards[1]]
    return boardCopy

def printMutilations(sideLength):               #Prints all correct boards to terminal.
    boards=uniqueCorrectMutilations(sideLength)
    for board in boards:
        board.printBoard()
        print()

def main():
    sideLength=8                # Set to 8 to match the brief, but works for any side length.
    printMutilations(sideLength)

main()





