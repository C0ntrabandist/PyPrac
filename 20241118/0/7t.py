class A:
    def __str__(self):
        return f"A"

class B(A):
    def __str__(self):
        return f"{super().__str__()}:B"

class C(B):
    def __str__(self):
        return f"{super().__str__()}:C"

print(C())