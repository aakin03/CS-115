'''
Feb 23, 2015
@author: Ayse Akin
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
'''

def helper(lst):
    '''Takes a list and creates a list of sums of adjacent terms in the original list'''
    if len(lst) == 1:
        return [1]
    return [lst[0]+lst[1]] + helper(lst[1:])

def pascal_row(n):
    '''Given a single integer, returns a list of of elements found in that row'''
    if n == 0:
        return [1]
    return [1] + helper(pascal_row(n-1))

def pascal_triangle(n):
    '''Given a single integer, returns a list of lists containing the values of all the rows up to and including row n'''
    if n < 0:
        return []
    return pascal_triangle(n-1) + [pascal_row(n)]