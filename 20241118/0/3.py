class A:
    __v = 0

    def inc(self):
        self.__v += 1
        print(self.__v)

    def __str__(self):
        return f"<{self.__v}>"


class B(A):
    def __init__(self):
        self.__v = 100500
#    __v = 100500


b = B()
b.inc()  # Выведется 1, так как используем "защищенные поля"
b.inc()
print(b._B__v, b._A__v)