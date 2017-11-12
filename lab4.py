'''
Created on Feb 19, 2015

@author: Ayse Akin
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
0

'''

def knapsack(capacity, itemList):
    '''Returns the max value of items that can be taken and then gives back a list of the items that you can take without going over the capacity.'''
    if capacity == 0:
        return [0, []]
    elif itemList == []:
        return [0, []]
    else:
        if itemList[0][0] > capacity:
            return knapsack(capacity, itemList[1:])
        else:
            loseIt = knapsack(capacity, itemList[1:])
            useIt = knapsack(capacity-itemList[0][0], itemList[1:])
            useIt = [itemList[0][1] + useIt[0], useIt[1] + [itemList[0]]]
            if useIt[0] > loseIt[0]:
                return useIt
            return loseIt
