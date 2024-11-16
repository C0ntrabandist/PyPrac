import sys

class Omnibus:
    all_attrs = {}
    
    def __init__(self):
        self.attrs = set()
    
    def __getattr__(self, attr):
        return Omnibus.all_attrs.get(attr, 0)
    
    def __setattr__(self, attr, value):
        if attr == 'attrs':
            super().__setattr__(attr, set())
        elif attr not in self.attrs:
            self.attrs.add(attr)
            Omnibus.all_attrs[attr] = Omnibus.all_attrs.get(attr, 0) + 1
    
    def __delattr__(self, attr):
        if attr in self.attrs:
            self.attrs.remove(attr)
            Omnibus.all_attrs[attr] -= 1


exec(sys.stdin.read())