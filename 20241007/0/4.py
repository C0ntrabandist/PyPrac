def rbin(n, l, cnt):
    
    if n == 1:
        print(*l + [cnt])
    else:
        rbin(n - 1, l + [cnt], 0)
        rbin(n - 1, l + [cnt], 1)


rbin(9, [], 1)

