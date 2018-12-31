"""
Name: pictureGrid.py,
Description: You can think of grid[x][y] as being the character at the x= and y=coordinates of a picture drawn with text characters. The (0, 0) origin will be in the upper-left corner, the x-coordinates increase going right and w the y-coordinates increase going down. Copy the previous grid value, and write the code that uses it to print the image.
Page: 103,
Date: 3/12/18,
Author: realJema,
Book: Automate the Boring stuff with python 2015,
"""

# Variables
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Functions
def drawPic(theGrid):
    x = len(theGrid)
    y = len(theGrid[1])

    for y1 in range(0, y):
        for x1 in range(0, x):
            print(theGrid[x1][y1], end='')
        print("")

# main
drawPic(grid)
