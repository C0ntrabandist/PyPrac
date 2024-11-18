from math import inf

def div_ab(a, b):
    if b == 13:
        raise ValueError("No 13 allowed")
    return a / b

def div(a, b):
    if abs(b) < 0.001:
        return ValueError(f" {b} - это же почти наверняка ноль!?!")
    c = a / b
    return -c

def proxy(func, *args):
    try:
        return func(*args)
    except ZeroDivisionError:
        return inf

for i in range(-10, 10, 2):
    print(proxy(div_ab, 152, i))


print(proxy(div, 100, 0.0001))