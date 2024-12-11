class dump(type):
    def __init__(cls, name, bases, attrs):
        def wrap(mth):
            def wrapped(self, *a, **k):
                print(f"{mth.__name__}: {a}, {k}")
                return mth(self, *a, **k)
            return wrapped
        for key, val in attrs.items():
            if callable(val):
                setattr(cls, key, wrap(val))
        super().__init__(name, bases, attrs)

import sys
exec(sys.stdin.read())