import math

def stepen(x, n: int):
    y = 1
    if n < 0:
        y /= stepen(x, -n)
    elif n > 0:
        if n & 1 != 0: y = x
        y *= stepen(x * x, n >> 1)
    return y 

def tower(n):
    '''
    The Tower of Hanoi
    '''
    m = 0
    def hanoi(n, f, t, s):
        nonlocal m
        if n > 0:
            hanoi(n - 1, f, s, t)
            m += 1
            print("%4d. Move disc %d from %s to %s" % (m, n, f, t))
            hanoi(n - 1, s, t, f)
    hanoi(n, "A", "B", "C")

def pascal(n, k):
    if k < 0 or n < k:
        return 0
    elif k == 0 or n == k:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)

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

def sqr(x):
    return x * x

def sqrt(x):
    if x == 0 or x == 1: return x
    t, s = 0, 1
    while t != s: 
        t, s = s, (s + x / s) / 2
    return s

ln2 = 0.69314718055994530941723212145817656807550013436026
log2 = 0.30102999566398119521373889472449302676818988146211
hi = sqrt(2)
lo = 1 / hi
ε = 0
π = 3.1415926535897932384626433832795

def ipower(x, n: int): 
    '''
    xⁿ
    '''
    y = 1
    if x == 1 or n == 0: return y
    if x == 0: return x
    r = n < 0
    if r: n = -n
    while True:
        if n & 1 != 0: y *= x
        n >>= 1
        if n == 0: break
        x *= x
    if r: y = 1 / y
    return y

def exp2(x):
    '''
    2^x
    '''
    y = 1
    n = int(x)
    x -= n
    if x < 0:
        n -= 1
        x += 1
    if x == 0.5:
        y *= hi
    elif x != 0:
        x *= ln2
        a = 1
        k = 0
        z = 0
        while abs(y - z) > ε:
            k += 1
            a *= x / k
            z = y
            y += a
    p = 1 << abs(n)
    if n < 0:
        y /= p
    else:
        y *= p
    return y

def exp(x):
    return exp2(x / ln2)

def lb(x):
    n = 0
    while x > hi:
        x /= 2
        n += 1
    while x < lo:
        x *= 2
        n -= 1
    x -= 1
    if x == 0: return n
    x /= x + 2
    q = x * x
    k = 1
    y = x
    z = 0
    while abs(y - z) > ε:
        z = y
        k += 2
        x *= q
        y += x / k
    y = 2 * y / ln2 + n
    return y

def ln(x):
    '''
    logarithmus naturalis
    '''
    return lb(x) * ln2

def log(x):
    n = 0
    while x >=10:
        x /= 10
        n += 1
    while x <= 0.1:
        x *= 10
        n -= 1
    return lb(x) * log2 + n

def NapLog(x):
    '''
    Napier Logarithm
    '''
    return -6931471.4590258570379728730284112684456223539106534 * lb(x / 10_000_000)

def power(x, y):
    '''
    x^y
    '''
    if x == 1 or y == 0: return 1
    if x == 2: return exp2(y)
    n = int(y)
    y -= n
    p = ipower(x, n)
    if y != 0:
        if y == 0.5: p *= sqrt(x)
        elif y == -0.5: p /= sqrt(x)
        else: p *= exp2(y * lb(x))
    return p

def root(x, y): 
    return power(x, 1/y)

def newton(n, k):
    if k == 0 or k == n: return 1
    if k == 1: return n
    if n == 0: return 0
    if k > 0:
        if n > 0:
            if k > n: return 0
            return newton(n - 1, k - 1) + newton(n - 1, k)
        else:
            return newton(n + 1, k) - newton(n, k - 1)
    else:
        if n > 0 or n < k: return 0
        return newton(n + 1, k + 1) - newton(n, k + 1)
        

# print(stepen(1 - 1/1000000, 1000000))

for k in range(6, -7, -1):
    for n in range(-7, 8):
        print("%5d" % (newton(n, k)), end = " ")
    print()
