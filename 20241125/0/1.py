def dumper(f):
    def newfun(*args):
        print(">", *args)
        res = f(*args)
        print("<", res)
        return res

    return newfun


def isint(fun):
    def wrapper(*args):
        if not all(isinstance(arg, int) for arg in args):
            raise TypeError("Not all int")
        return fun(*args)
    return wrapper


@isint
@dumper
def fun(a, b):
    return a * 2 + b


print(fun(2, 3))
print(fun(2, "str"))