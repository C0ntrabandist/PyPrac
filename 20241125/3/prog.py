class Vowel:
    __slots__ = list("aeiouy")
    
    def __init__(self, **kwargs):
        for kwarg in kwargs:
            setattr(self, kwarg, kwargs[kwarg])

    @property
    def full(self):
        return all(hasattr(self, a) for a in self.__slots__)

    @full.setter
    def full(self, val):
        pass

    @property
    def answer(self):
        return 42

    def __str__(self):
        return ", ".join(f"{a}: {getattr(self, a)}" for a in self.__slots__ if hasattr(self, a))


import sys
exec(sys.stdin.read())