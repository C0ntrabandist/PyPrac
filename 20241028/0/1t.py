from itertools import count

def fun(a):
    for i in range(a):
        print(">>")
        yield f"<{i}>"
        print("<<")
'''
res = fun(4)
n = next(res)
print(n)
n = next(res)
print(n)
n = next(res)
print(n)
n = next(res)
print(n)
n = next(res)
'''
def func():
    result = 0
    for n in count(1):
        result += 1 / n ** 2
        yield result

f = func()
for i in range(count):
    print(next(f))