from math import *

def minf(*args):
    def func(x):
        return min(i(x) for i in args)

    return func

#f = minf(math.sin, math.sqrt)
#print(f(0))
