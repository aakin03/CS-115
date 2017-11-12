def length(lst):
    if lst == []:
        return 0
    return 1 + length(lst[1:])

def dot(L, K):
    if L == [] or K == []:
        return 0.0
    else:
        return (L[0] * K[0]) + dot(L[1:], K[1:])
    "The function compiles the dot product of the two lists, L and K" 
    "Inputs are the two lists of numbers which the function then finds the dot product of."

def explode(S):
    if S == "":
        return []
    else:
        return [S[0]] + explode(S[1:])
    'The function takes the string inputed and returns one total list made up of each character as a separate entity in the list'

def ind(e, L):
    if L == [] or L == "" or L[0] == e:
        return 0
    else:
        return 1 + ind(e, L[1:])
        
def removeAll(e, L):
    if L == []:
        return []
    elif L[0] == e:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:]) 
    'The function takes an element and a list then goes through the list to see if the element is in it and returns the list without the element.'

print removeAll(5, [1,2,3,4,5])

def even(n):
    if n % 2 == 0:
        return True
    return False

def myFilter(f, L):
    if L == []:
        return []
    else:
        if f(L[0]) == True:
            return [L[0]] + myFilter(f, L[1:])
        else:
            return myFilter(f, L[1:])
    'The function takes another function and a list then uses the function to go through the list to do whatever the purpose of the other function is.'
    
def deepReverse(L):
    if L == []:
        return []
    else:
        if isinstance(L[-1], list):
            return [deepReverse(L[-1])]+ deepReverse(L[:-1])
        return [L[-1]] + deepReverse(L[:-1])

print deepReverse([2,1,[4,1,10],5])
