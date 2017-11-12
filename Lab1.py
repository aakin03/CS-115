import math
def inverse(x):
    return 1.0/x

def addIt(x, y):
    return x + y

def e(x):
    return reduce(addIt, map(inverse, map(math.factorial, range(x+1))))
    
def error(n):
    return abs(math.e-e(n))