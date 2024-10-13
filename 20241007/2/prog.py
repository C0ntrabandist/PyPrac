def sub_objects(a, b):
    if not isinstance(a, type(b)):
        raise TypeError()
    
    if isinstance(a, (int, float)):
        return a - b
    elif isinstance(a, (list, tuple)):
        result = [item for item in a if item not in b]
        return type(a)(result)
    else:
        raise TypeError()

a, b = eval(input())
print(sub_objects(a, b))
