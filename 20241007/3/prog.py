from math import *

def Calc(s, t, u):
    sf = eval(f"lambda x: {s}")
    tf = eval(f"lambda x: {t}")
    uf = eval(f"lambda x, y: {u}")
    
    def resultf(x):
        return uf(sf(x), tf(x))
    
    return resultf

s, t, u = input().replace('"', '').split(',')
x = eval(input())
F = Calc(s, t, u)
print(F(x))
