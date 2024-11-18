from math import inf

def div_ab(a, b):
    c = a / b
    return c

def proxy(func, *args):
    try:
        return func(*args)
    except ZeroDivisionError:
        return inf

for i in range(-10, 10, 2):
    print(proxy(div_ab, 152, i))
