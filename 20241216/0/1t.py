def ite(n):
    res = 0
    for i in range(n):
        param = yield i
        res += param

def call(ite, n):
    res = yield from ite (n)
    yield res