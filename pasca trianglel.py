def fib(n):
    if n > 1:
        return fib(n - 2) + fib(n - 1)
    elif n < 0: 
        return fib(n + 2) - fib(n + 1)
    else:
        return n

def fact(n):
    if n > 1:
        return n * fact(n - 1)
    else:
        return 1

def pascal(n, k):
    '''
    ## Pascal triangle
    '''
    if k < 0 or n < k:
        return 0
    elif k == 0 or n == k:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)

def newton(n, k):
    '''
    ## Pascal triangle (Newton extension)
    '''
    if k == 0 or k == n: return 1
    if k == 1: return n
    if n == 0: return 0
    if k > 0:
        if n > 0:
            if k > n: return 0
            return newton(n - 1, k - 1) + newton(n - 1, k)
        return newton(n + 1, k) - newton(n, k - 1)
    if n > 0 or n < k: return 0
    return newton(n + 1, k + 1) - newton(n, k + 1)
        
for k in range(6, -7, -1):
    for n in range(-7, 8):
        print("%5d" % (newton(n, k)), end = " ")
    print()
