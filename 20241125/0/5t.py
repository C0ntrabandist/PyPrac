class Dsc:

    def __get__(self, obj, cls):
        print(f"Get from {cls}:{repr(obj)}")
        return obj._value

    def __set__(self, obj, val):
        print(f"Set in {repr(obj)} to {val}")
        obj._value = val

    def __delete__(self, obj):
        print(f"Delete from {repr(obj)}")
        obj._value = None

class C:
        def __get__(self, obj, cls):
            print("GET", obj)

        def __set__(self, obj, value):
            print("SET", obj, value)
            obj._value = value

        def __delete__(self, obj):
            print("DELETE", obj)

class D:
     desrc = C()

d = D()
d.desrc = 123
print(d.desrc)
del d.desrc