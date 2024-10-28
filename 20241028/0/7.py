from itertools import filterfalse

n = int(input("N = "))
r = range(11, 101)
print(*filterfalse(lambda x: x % n, r))