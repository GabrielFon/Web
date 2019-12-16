#  File: MagicSquares.py
#  Description: Homework 13
#  Student's Name: Gabriel Fonseca
#  Student's UT EID: gcf359
#  Course Name: CS 303E 
#  Unique Number: 50070
#
#  Date Created: 11/13/2019
#  Date Last Modified: 11/15/2019


class MagicSquare:

    def __init__(self, side):

        self.sideLength = side
        row = []
        grid = []

        for rowcount in range(side):

            row = [] # create a new row
        
        
            for column in range(side):
                row.append(0)

            grid.append(row)

        self.grid = grid

        i = 1
        length = self.sideLength
        rowposition = 0
        colposition = length//2
        

        while i != (length**2+1):
        
            self.grid[rowposition][colposition] = i

            if ((i % length) == 0):
                rowposition += 1
                
            else:
                
                if (rowposition == 0) and (colposition < (length - 1)):
                    rowposition = length - 1
                    colposition += 1
                    
                elif (colposition == (length - 1)) and (rowposition != 0):
                    colposition = 0
                    rowposition -= 1
                    
                elif (colposition == (length - 1)) and (rowposition == 0):
                    rowposition = length - 1
                    colposition = 0

                else:
                    rowposition -= 1
                    colposition += 1

            i = i + 1
        
            
        
        

    def display(self):

        if (str(self.grid[0]).isdigit()) == False: 
            numRows = len(self.grid)
            numColumns = len(self.grid[0])

            for row in range(numRows):
                for col in range(numColumns):
                    print(format(self.grid[row][col], "5d"), end = "")

                print("")

        else:

            for col in range(len(self.grid)):
                print(format(str(self.grid[col]), "5d"), end = "")

        return 


def main():

    for k in range(1, 14, 2):
        s = MagicSquare(k)
        print("Magic Square of size", k)
        print()
        s.display()
        print()
        

main()

    
