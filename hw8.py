'''
Mar 30, 2015
@author: Ayse Akin
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
CS - 115 Hw8
'''

def TcToNum(s):
    ''' Converts a string of two's compliment representation into a decimal number.'''
    def TcToNum_Helper(s):
        '''Converts a string starting from the second bit until the end, into a decimal number'''
        if s == "":
            return 0
        else:
            if s[-1] == '0':
                return 2 * TcToNum_Helper(s[:-1])
            else:
                return 2 * TcToNum_Helper(s[:-1]) + 1
    if s[0] == '1':
        return TcToNum_Helper(s[1:]) - 128
    return TcToNum_Helper(s)

def isOdd(n):
    '''checks if a number is odd'''
    if n % 2 == 0:
        return False
    else:
        return True
    
def NumToTc(n):
    '''Converts a given decimal number into a two's compliment representation.'''
    def NumToTc_Helper(n):
        '''Converts a positive version of the decimal number into a binary representation.'''
        if n == 0 or n < 0:
            return ''
        if isOdd(n):
            return NumToTc_Helper(n/2) + '1'
        if isOdd(n) == False:
            return NumToTc_Helper(n/2) + '0'
    if n < -128 or n > 127:
        return 'Error'
    if n < 0:
        return '1' + NumToTc(n+128)[1:]
    else:
        if len(NumToTc_Helper(n)) < 8:
            return '0' * (8-len(NumToTc_Helper(n))) + NumToTc_Helper(n)