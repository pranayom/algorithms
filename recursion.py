def sum_n(n):

    if n <= 1:
        return n
    else:
        return n + sum_n(n-1)
    
print(sum_n(10))


# Recursion Design Gurus