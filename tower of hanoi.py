def tower(n):
    '''
    ## The Tower of Hanoi
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

tower(3)