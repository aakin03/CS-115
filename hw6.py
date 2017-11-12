'''
Created on 10 March 15
@author:   Ayse Akin, Jennifer Cafiero
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System."

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.

def isOdd(n):
    '''checks if a number is odd'''
    if n % 2 == 0:
        return False
    else:
        return True

def numToBinary(N):
    '''converts a given decimal number into a string bits'''
    if N == 0:
        return ''
    if isOdd(N):
        return numToBinary(N/2)+'1' 
    else:
        return numToBinary(N/2)+'0'
print numToBinary(64)

def binaryToNum(S):
    '''converts a string of binary digits into a decimal'''
    if S == '':
        return 0
    elif S[-1] == '0':
        return 2 * binaryToNum(S[:-1])
    else:
        return 2 * binaryToNum(S[:-1]) + 1


k = 5 #sets number of bits
a = 2**k -1 #largest number that can be represented with k number of bits

def countme(s):
    '''counts the number of repeated digits'''
    if s == '':
        return 0
    elif len(s) == 1:
        return 1
    elif s[0] == s[1]:
        return 1 + countme(s[1:])
    else:
        return 1

def listme(s):
    '''turns the string into a list with the digit as the first part and the number of times it appears in the series in a row'''
    if s == '':
        return []
    n = countme(s)
    return breakme([s[0],n]) + listme(s[n:])

def breakme(L):
    '''if the list is has a second element bigger than the encoding will allow, it breaks it up'''
    if L[1] > a:
        L = [[L[0],a]] + breakme([L[0],L[1]-a])
        return L 
    else:
        return [L]

def makeKBits(n):
    '''changes a binary number into a binary with k bits'''
    if len(numToBinary(n)) <= COMPRESSED_BLOCK_SIZE:
        return '0'* (COMPRESSED_BLOCK_SIZE-len(numToBinary(n))) + numToBinary(n)

def printme(L):
    '''prints one section of the list into the encoded part'''
    if L[0] == '0':
        return '0' + makeKBits(L[1])
    else:
        return '1' + makeKBits(L[1])

def combineStrings(L):
    '''creates a string by combining the strings in the entered list'''
    if L ==[]:
        return ''
    return L[0] + combineStrings(L[1:])

def compress(s):
    '''compresses a sequence of binary digits into a condensed version'''
    x = listme(s)
    y = map(printme,x)
    return combineStrings(y)[1:]

def uncompress(s):
    '''takes a compressed sequence of binary digits and uncompresses them'''
    if s == '':
        return ''
    else:
        return s[0] * binaryToNum(s[1:COMPRESSED_BLOCK_SIZE+1]) + uncompress(s[COMPRESSED_BLOCK_SIZE+1:])

def compression(s):
    '''finds the ratio of the compressed string to the uncompressed string'''
    return float(len(compress(s)))/len(s)



#The largest number of bits that could be used to encode a 64-bit string would be 128 bits. 

#Professor Lai is Lai-ing because if there is a string like, '10' * 32, it will return a much longer string
#in comparison to its input. It would return '0000000001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001'
#which as you can see is much longer than 64 digits. 
compress('0110' * 16)