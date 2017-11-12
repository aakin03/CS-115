def mult(x,y):
    #Function that multiplies two numbers
    return x * y

def factorial(n):
    #Function that finds factorial of a number
    if n > 1:
        return reduce(mult, range(1, n+1))
    return 1

def add(x,y):
    #Fnction that adds two numbers
    return x+y

def mean(L):
    #Function that finds the mean of a list of numbers
    return reduce(add, L)/(len(L))

def divides(n):
    def div(k):
        return n % k == 0
    return div
    
def prime(n):
    #Returns boolean if number is a prime number
    return (True not in map(divides(n), range(2, n-1)))
