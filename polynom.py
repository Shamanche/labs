def polynom(n, x):
    if n == 0:
        return 1 # P0 = 1
    elif n == 1:
        return x # P1 = x
    else:
        res = (((2 * n)-1)*x * polynom(n-1, x)-(n-1)*polynom(n-2, x))/float(n)
        print(res)
        return res