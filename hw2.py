'''
Created on Feb 5, 2015
@author: Ayse Akin
Pledge: I pledge my honor that I have abided by the Stevens Honors System.

CS 115 - Hw 2
'''
import sys

#Allows up to 10000 recursive calls
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]
   
Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']


def letterScore(letter, scorelist):
    '''Returns the point value of a letter based on a scorelist.'''
    if scorelist[0][0] == letter:
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])
    
def wordScore(S, scorelist):
    '''The function takes a string as input and returns the value of the word from a scorelist.'''
    if S == "":
        return 0
    else:
        return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def removeWord(letter, Rack):
    '''Takes the letter given by the possibleWord function and goes through the Rack until it finds the letter'''
    if Rack == []:
        return []
    elif letter == Rack[0]:
        return Rack[1:]
    return [Rack[0]] + removeWord(letter, Rack[1:])

def possibleWord(word, Rack):
    '''Taking the word inputed and seeing if you can make the word from the letters given'''
    if word == "":
        return True
    elif Rack == []:
        return False
    elif word[0] in Rack:
        return possibleWord(word[1:], removeWord(word[0], Rack))
    return False

def showWords(Rack, word):
    '''Returns the possible words that can be made using the letters in the Rack'''
    if word == "":
        return []
    elif possibleWord(word, Rack):
        return [word, wordScore(word, scrabbleScores)]

def getScores(Rack, myDictionary):
    '''Takes a rack of letters and returns the score of each word that can possibly be made using those letters'''
    if myDictionary == []:
        return [] 
    elif showWords(Rack, myDictionary[0]):
        return [showWords(Rack, myDictionary[0])] + getScores(Rack, myDictionary[1:])
    else:
        return getScores(Rack, myDictionary[1:])
    
def scoreList(Rack):
    '''Returns the result from getScores when given only the letters in the Rack'''
    return getScores(Rack, Dictionary)

def maxPoints(x, y):
    '''Determines which word has the highest point value'''
    if x[1] < y[1]:
        return y
    return x

def bestWord(Rack):
    '''Returns the word with the highest point value that can be made out of the letters in the Rack'''
    if Rack == []:
        return []
    elif scoreList(Rack) == []:
        return ['', 0]
    return reduce(maxPoints, scoreList(Rack))
