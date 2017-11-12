'''
Created on Apr 9, 2015

@author: Ayse Akin
Pledge: I pledge my honor that I have abided by the Stevens Honors System.
CS 115 - Lab 10
'''
import sys
import random
from _sqlite3 import Row

def createOneRow(width):
    '''returns one row of zeros of width "width" ...
    You might use this in your createBoard(width, height) function '''
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    ''' returns a 2d array with "heigth" rows and "width" cols '''
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

def printBoard(A):
    ''' this function prints the 2d list-of-Lists
    A without spaces (using sys.stdout.write) '''
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write ('\n')

def diagonalize(width, height):
    ''' creates an empty board and then modifies it
    so that it ahs a diagonal strip of "on" cells. '''
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w, h):
    '''returns a 2d array of all live cells - with the value of 1
    - except for a one-cell-wide border of empty cells around the
    edge of the 2d array'''
    A = createBoard(w, h)
    for row in range(1, h-1):
        for col in range(1, w-1):
            A[row][col] = 1
    return A

def randomCells(w, h):
    '''returns an array of randomly-assigned 1's and 0's except
    with the outer edge of the array is completely empty'''
    A = createBoard(w, h)
    for row in range(1, h-1):
        for col in range(1, w-1):
            A[row][col] = random.choice ( [0,1])
    return A

def copy(A):
    '''Deep copies A into newA'''
    newA = createBoard(len(A[0]), len(A))
    for row in range(len(A)):
        for col in range(len(A[0])):
            newA[row][col] = A[row][col]
    return newA

def innerReverse(A):
    '''Takes an old 2d array and then creates a new
    array of the same shape and size where, excluding the border,
    the 1's from the old array are changed to 0 in the new array
    and the 0's from the old array are changed to 1 in the new array'''
    newA = createBoard(len(A[0]), len(A))
    for row in range(1, len(A)-1):
        for col in range(1, len(A[0])-1):
            if A[row][col] == 1:
                newA[row][col] = 0
            if A[row][col] == 0:
                newA[row][col] = 1
    return newA
    
def countNeighbors(row, col, A):
    ''' Returns the number of live neighbors for a cell'''
    n = 0
    if A[row-1][col-1] == 1:
        n += 1        
    if A[row-1][col] == 1:
        n += 1
    if A[row-1][col+1] == 1:
        n += 1
    if A[row][col-1] == 1:
        n += 1
    if A[row][col+1] == 1:
        n += 1
    if A[row+1][col-1] == 1:
        n += 1
    if A[row+1][col] == 1:
        n += 1
    if A[row+1][col+1] == 1:
        n += 1
    return n

def next_life_generation(A):
    ''' makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0.'''
    newA = copy(A)
    for row in range(1, len(A)-1):
        for col in range(1, len(A[0])-1):
            if A[row][col] == 1:
                if countNeighbors(row, col, A) < 2 or countNeighbors(row, col, A) > 3:
                    newA[row][col] = 0
            if A[row][col] == 0:
                if countNeighbors(row, col, A) == 3:
                    newA[row][col] = 1
    return newA



