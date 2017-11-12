'''
Created on: 6 March 15
@author:   Ayse Akin
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n == 0:
        return False
    if n%2 == 1:
        return True
    return False

#00101010 -> base-2 representation of 42.

#If you are given an odd base-10 number, the least significant bit will be 1 in the base-2 representation.
#However, if you are given an even base-10 number, the least significant bit will be 0 in the base-2 representation.

#If the original base-2 representation translates to an odd base-10 number, 1 is subtracted and then divided by 2.
#If the original base-2 representation translates to an even base-10 number, the number is divided by 2.

#If N is odd, n/2 will tell us to add a 1 to the end of the base-2 number.
#If N is even, n/2 will tell us to add a 0 to the end of the base-2 number.

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if isOdd(n):
        return numToBinary(n/2) + "1"
    else:
        return numToBinary(n/2) + "0"

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    def binaryToNum_helper(s, c):
        if s == "":
            return 0
        if int(s[-1]) == 0:
            return binaryToNum_helper(s[:-1], c + 1)
        return binaryToNum_helper(s[:-1], c + 1) + 2 **c
    return binaryToNum_helper(s, 0) 
        
def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if len(numToBinary(binaryToNum(s) + 1)) < 8:
        return "0" * (8 - len(numToBinary(binaryToNum(s) + 1))) + numToBinary(binaryToNum(s) + 1)
    elif len(numToBinary(binaryToNum(s) + 1)) > 8:
        return numToBinary(binaryToNum(s) + 1)[1:]
    return numToBinary(binaryToNum(s) + 1)

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print s
    if n == 0:
        return s
    return count(increment(s), n-1)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    return numToTernary(n/3) + str(n % 3)

#The ternary representation for 59 is 2012. (2*1) + (1*3) + (0*9) + (2*27) = 59 

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    def ternaryToNum_helper(s, c):
        if s == "":
            return 0
        if int(s[-1]) == 0:
            return ternaryToNum_helper(s[:-1], c + 1)
        return ternaryToNum_helper(s[:-1], c + 1) + (int(s[-1])) *3 **c
    return ternaryToNum_helper(s, 0)