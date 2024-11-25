def dumper(f):
    def newfun(*args, **kwargs):
        print(">", *args, **kwargs)
        res = f(*args, **kwargs)
        print("<", res)
        return res

    return newfun