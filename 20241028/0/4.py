from random import randint

def walk2d(x = 0, y = 0):
    while True:
        coord = (yield (x, y))
        x, y = x + coord[0], y + coord[1]

g = walk2d()
print(next(g))
#print(g.send(None))

for n in range(5, -1, -1):
    print(g.send((1, 1)))
'''
while True:
    print(g.send((randint(-5, 5), randint(-5, 5))))
'''
'''
print(g.send((1, 1)))
print(g.send((1, 0)))
print(g.send((2, 3)))
print(g.send((4, 12)))
print(g.send((100, 82)))
'''        