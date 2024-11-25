class slo:
    __slots__ = "a", "b", "c"
    ro = "Read Only"

    def __init__(self, a, b, c):
        for attr in self.__slots__:
            setattr(self, attr, attr)

c = slo(5, 7, 8)
print(c.a)
print(c.ro)
dir(slo)
print(c.__slots__)