def factorial(n):
    """
        Base case,      n = 0, once base case is reached, no more recursive calls are made
        Recursive case, n >= 1
    """
    if n == 0:  
        return 1
    else:
        return n * factorial(n-1)

