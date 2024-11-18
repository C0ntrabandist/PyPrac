#Wrong
class A:
    pass

class B(A):
    pass

class X(A, B):
    pass

#Right
class A:
    pass

class B(A):
    pass

class X(B, A):
    pass