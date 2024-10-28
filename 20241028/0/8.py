from itertools import repeat, chain

def repeater(seq, n):
    yield from chain.from_iterable(map(lambda x: repeat(x, n), seq))

print(*repeater("QWE", 10))

print(*repeater(['QWE', 'RTY'], 5))

def repeater2(seq, n):
    for el in n:
        yield from repeat(el, n)


print(*repeater("QWE", 5))