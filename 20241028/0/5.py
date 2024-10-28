def travel(n):
    for i in range(n):
        yield "по кочкам"
    return "и в яму"

def travelwrap(n):
    s = yield from travel(n)
    yield s

g = travelwrap(10)
for i in g:
    print(i)

for s in travel(3):
    print(s)