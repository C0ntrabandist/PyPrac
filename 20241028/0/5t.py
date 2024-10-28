def gen(n):
    for i in range(n):
        yield i*2+1
    return "Done"
'''
res = gen(4)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
'''
def gen2(a, b):
    yield from a
    yield from b
'''
new_d = list(gen2("QWE", gen(4)))
print(new_d)
'''
def gen3(string):
    yield from string
    return len(string)
'''
g = gen3("QWE")
print(next(g))
print(next(g))
print(next(g))
'''
def wrap(string):
    res = yield from gen3(string)
    print("Result: ", res)

for s in wrap("QWER"):
    print(s)

res_new = list(wrap("QWERTTYUIO"))
print(res_new)