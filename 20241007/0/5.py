import math

def s(f, g):

    def func(x):
        return f(x) + g(x)

    return func

res = s(math.sin, math.cos)
print(res(math.pi / 4))
