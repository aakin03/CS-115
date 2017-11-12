'''
Created on 2 March 15
@author:   Ayse Akin
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 5
'''
import turtle # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.

def svTree(trunkLength, levels):
    '''Takes a desired initial trunk length and a desired number of levels and
    returns a tree with a number of levels the branches of the tree should extend to.
    i.e. one level is just the trunk, two levels is a trunk and then two branches off the trunk, etc.'''
    if levels != 0:
        turtle.shape("turtle")
        turtle.width(trunkLength/5)
        turtle.pencolor("brown")
        turtle.forward(trunkLength)
        turtle.left(45)
        turtle.pencolor("green")
        svTree(trunkLength/2.0, levels-1)
        turtle.right(90)
        svTree(trunkLength/2.0, levels-1)
        turtle.left(45)
        turtle.backward(trunkLength)
        turtle.pencolor("brown")

def fastFib(n):
    '''Returns the nth Fibonacci number using the memoization technique
    shown in class and lab. Assume that the 0th Fibonacci number is 0, so
    fastFib(0) = 0,
    fastFib(1) = 1, and
    fastFib(2) = 1'''
    def fastFib_helper(n, memo):
        if n in memo:
            return memo[n]
        if n == 0:
            result = 0
        if n == 2 or n == 1:
            result = 1
        else:
            result = fastFib_helper((n-1), memo) + fastFib_helper((n-2), memo)
        memo[n] = result
        return result
    return fastFib_helper(n, {})
            

# If you did this correctly, the results should be nearly instantaneous.
print fastFib(3)  # 2
print fastFib(5)  # 5
print fastFib(9)  # 34
print fastFib(24)  # 46368
print fastFib(40)  # 102334155
print fastFib(50)  # 12586269025

# Should take a few seconds to draw a tree.
svTree(128, 6)