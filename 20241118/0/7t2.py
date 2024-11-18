class A:
    def __str__(self):
        return "A"

class B(A):
    def __str__(self):
        return f"{super().__str__()}:{self.__class__.__name__}

class C(B):
    def __str__(self):
        return f"C:{super().__str__()}"

print(C())