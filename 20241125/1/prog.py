def objcount(cls):
    class New(cls):
        counter = 0
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__class__.counter += 1

        def __del__(self):
            self.__class__.counter -= 1
            if hasattr(super(), '__del__'):
                super().__del__()
                
    return New

import sys
exec(sys.stdin.read())