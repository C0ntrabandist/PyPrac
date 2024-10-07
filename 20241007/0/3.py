def rec(n):
    if n == 0:
        exit()
    else:
        print(f"Now {n}")
        return rec(n - 1)

rec(10)
