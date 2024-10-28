from itertools import *

g = list(product("QW", "rt", [0,1]))
print(g)

p = list(permutations("QWER", 2))
print(p)