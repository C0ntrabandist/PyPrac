from itertools import *

print([f'{v}{h}' for v, h in list(product('ABCDEFGH', range(1, 9)))]) #ABCDEFGH

chess = [f'{v}{h}' for v, h in list(product('ABCDEFGH', range(1, 9)))]

for cell in chess:
    print(cell)