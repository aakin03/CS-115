'''
Created on Feb 12, 2015
@author: Ayse Akin
Pledge: I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 3
'''

''' Problem 0 '''
def giveChange(amount, coins):
    '''Returns the minimum number of coins needed to give the amount of change, followed
    by what coins are needed to give back that change''' 
    if amount == 0:
        return [0, []]
    elif coins == []:
        return [float("inf"), []]
    else:
        if coins[0] > amount:
            return giveChange(amount, coins[1:])
        else:
            loseIt = giveChange(amount, coins[1:])
            useIt = giveChange(amount-coins[0], coins)
            useIt = [1+ useIt[0], useIt[1] + [coins[0]]]
            if useIt[0] > loseIt[0]:
                return loseIt
            return useIt
        
print giveChange(48, [1, 5, 10, 25])

scrabbleScores = \
    [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
      ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
      ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
      ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

''' Problem 1 '''
def letterScore(letter, scorelist):
    '''Returns the point value of a letter based on a scorelist.'''
    if scorelist[0][0] == letter:
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])
    
def wordScore(word, scorelist):
    '''The function takes a string as input and returns the value of the word from a scorelist.'''
    if word == "":
        return 0
    return letterScore(word[0], scorelist) + wordScore(word[1:], scorelist)

def wordsWithScore(dct, scores):
    '''Returns the dictionary with the score of every word in it'''
    if dct == []:
        return []
    return [[dct[0], wordScore(dct[0], scores)]] + wordsWithScore(dct[1:], scores)  

''' Problem 2 '''

def take(n, L):
    '''Returns the list from the beginning until the index the user inputs is reached'''
    if L == [] or n == 0:
        return []
    return [L[0]] + take(n-1, L[1:])

''' Problem 3 '''

def drop(n, L):
    '''Returns the list starting from the index the user chooses until the end'''
    if L == []:
        return []
    if n > 0:
        return drop(n-1, L[1:])
    return [L]