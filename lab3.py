'''
Created on Feb 12, 2015

@author: Ayse Akin
'''

def minimum(x, y):
    if x < y:
        return x
    return y

def change(amount, coins):
    if amount == 0:
        return 0
    elif coins == []:
        return float("inf")
    else:
        firstCoin = coins[0]
        if firstCoin > amount:
            return change(amount, coins[1:])
        else:
            useIt = 1 + change(amount-firstCoin, coins)
            loseIt = change(amount, coins[1:])
    return minimum(useIt, loseIt)

print change(48, [1,5,10,25])

