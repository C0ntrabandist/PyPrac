def lin(a, b):
 
    def func(x):
        return a * x + c
    print(func.__closure__)
    c = a + b
    return func
    
