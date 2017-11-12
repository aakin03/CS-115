'''
Created on Mar 23, 2015

@author: Ayse Akin
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
'''
'''Part 1'''
def numToBaseB(N, B):
    if N == 0:
        return '0'
    if N/B == 0 and N > 0:
        return str(N%B)
    return numToBaseB(N/B, B) + str(N%B)

'''Part 2'''
def baseBToNum(S, B):
    if B == 10:
        return S
    def baseBToNum_helper(S, B, L):
        if S == "":
            return 0
        if int(S[-1]) == 0:
            return baseBToNum_helper(S[:-1], B, L + 1)
        return baseBToNum_helper(S[:-1], B, L + 1) + B**L
    return baseBToNum_helper(S, B, 0)

print baseBToNum('1203', 6)

'''Part 3'''
def baseToBase(B1, B2, SinB1):
    return numToBaseB(int(baseBToNum(SinB1, B1)), B2)

'''Part 4'''
def add(S, T):
    return numToBaseB(baseBToNum(S, 2) + baseBToNum(T, 2), 2)

'''Part 5'''
def addB(S, T):
    def sameLength(S, T):
        if len(S) == len(T):
            return S, T
        elif len(S) < len(T):
            return '0' * (len(T)-len(S)) + S,T
        return S, '0' * (len(S)-len(T)) + T
    
    def carryHelper(S, T, carry):
        if S == '':
            if carry == 0:
                return ''
            return '1'
        elif int(S[-1]) + int(T[-1]) + carry == 0:
            return carryHelper(S[:-1], T[:-1], 0) + '0'
        elif int(S[-1]) + int(T[-1]) + carry == 1:
            return carryHelper(S[:-1], T[:-1], 0) + '1' 
        elif int(S[-1]) + int(T[-1]) + carry == 2:
            return carryHelper(S[:-1], T[:-1], 1) + '0' 
        elif int(S[-1]) + int(T[-1]) + carry == 3:
            return carryHelper(S[:-1], T[:-1], 1) + '1'
    S = sameLength(S, T) [0]
    T = sameLength(S, T) [1]
    return carryHelper(S, T, 0)