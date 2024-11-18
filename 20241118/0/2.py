class A:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return self.__class__(self.val + other.val)
    
    def __str__(self):
        return f"<{self.val}>"


class B(A):
    def __str__(self):
        return f"[{self.val}]"

    def __sub__(self, other):
        return self.__class__(self.val - other.val)


a, b = B(7), B(9)
print(a, b)
print(a + b)

d = B(5)
c = A(4)
print(d + B(43) - c)