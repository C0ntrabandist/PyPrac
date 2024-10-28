def fun():
    i = 1
    result = 0
    while True:
        result += 1 / i ** 2
        i += 1
        yield result

f = fun()
for i in range(int(input())):
    print(next(f))