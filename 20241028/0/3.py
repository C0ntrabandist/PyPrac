def pgen():
    print('::')
    res = yield 'start'
    print(">")
    while res := (yield f"f/{res}"):
        print(">>")
    yield 'finish'
    print('<')


g = pgen()
next(g)

for c in range(5, -1, -1):
    print(g.send(c))