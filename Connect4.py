'''
Created on Apr 27, 2015

@author: Ayse Akin
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
'''

class Board(object):
    def __init__(self, width, height):
        '''Constructor method which initialized
        the two-dimensional array of space characters'''
        self.width = width
        self.height = height
        theBoard = []
        for row in range(self.height):
            l = []
            for col in range(self.width):
                l += [" "]
            theBoard+=[l]
        self.theBoard = theBoard

    def __str__(self):
        '''Returns a string representing the board'''
        r = ''
        for row in range(len(self.theBoard)):
            for col in range(len(self.theBoard[row])):
                r += '|' + self.theBoard[row][col]
            r += "|"+ "\n"
        r += (self.width*"--") +"-"+ "\n"
        r += " "
        for i in range(len(self.theBoard[1])):
            r += str(i) + " "
        return r
    
    def allowsMove(self, col):
        '''Checks to see if there is space left in a specified column
        and if the column is a valid column.'''
        if col <= self.width-1:
            for rows in self.theBoard:
                if rows[col] == " ":
                    return True
        return False
    
    def lowest(self, col):
        '''Looks for the physically lowest available
        row in a specified column'''
        for row in range((self.height-1), -1, -1):
            if self.theBoard[row][col] == " ":
                return row
        return False
    
    def addMove(self, col, ox):
        '''Adds a specified letter (ox) in
        the lowest row of a specified column'''
        self.theBoard[self.lowest(col)][col] = ox

    def setBoard(self, move_string):
        """ takes in a string of columns and places
        alternating checkers in those columns,
        starting with 'X'
        For example, call b.setBoard('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.setBoard('000000') to
        see them alternate in the left column.
        moveString must be a string of integers"""
        nextCh = 'X'   # start by playing 'X'
        for colString in move_string:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
                if nextCh == 'X':
                    nextCh = 'O'
                else:
                    nextCh = 'X'
        return self.theBoard
    
    def delMove(self, col):
        '''Deletes a specified letter (ox) in
        the lowest row of a specified column'''
        self.theBoard[self.lowest(col)+1][col] = " "
    
    def winsFor(self, ox):
        '''Returns true if there are four of the same checker (ox)
        in a row, column, or either way diagonally.'''
        for row in range(self.height):
            for i in range(self.width-3):
                if self.theBoard[row][i] == self.theBoard[row][i+1]\
                 == self.theBoard[row][i+2] == self.theBoard[row][i+3] == ox:
                    return True
        for col in range(self.width):
            for row in range(self.height-3):
                if self.theBoard[row][col] == self.theBoard[row+1][col]\
                 == self.theBoard[row+2][col] == self.theBoard[row+3][col] == ox:
                    return True
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.theBoard[row][col] == self.theBoard[row+1][col+1]\
                == self.theBoard[row+2][col+2] == self.theBoard[row+3][col+3] == ox:
                    return True
        for row in range(self.height-1, 2, -1):
            for col in range(self.width-3):
                if self.theBoard[row][col] == self.theBoard[row-1][col+1]\
                == self.theBoard[row-2][col+2] == self.theBoard[row-3][col+3] == ox:
                    return True
            
    def hostGame(self):
        '''Runs a loop allowing the user(s) to play
        a game of Connect 4.'''
        print "Welcome to Connect 4!"
        print self
        ox = "X"
        while (1):
            col = input(ox + "'s Choice: ")
            if Board.allowsMove(self, col) == False :
                print "Hi. This is wrong. This column is full or\
 may not be a valid column. Please pick another one."
            else:
                Board.addMove(self, col, ox)
                print self
                if Board.winsFor(self, ox):
                    print ox + " is the winner!"
                    break
                if ox == "X":
                    ox = "O"
                else:
                    ox = "X"
            
b = Board(8, 6)
print b
b.addMove(3,"x")
print b
b.delMove(3)
print b