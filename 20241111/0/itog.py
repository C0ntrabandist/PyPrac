class Rectangle:    
    rectcnt = 0
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        #Rectangle.rectcnt += 1
        self.__class__.rectcnt += 1
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        setattr(self, f"rect_{self.__class__.rectcnt}", self.rectcnt)

    def __str__(self):
        return f"({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1}) -- {Rectangle.rectcnt}"

    def __abs__(self):
        return (abs(self.x2 - self.x1) * (self.y2 - self.y1))

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __eq__(self, other):
        return abs(self) == abs(other)
    
    def __mul__(self, n):
        return self.__class__(self.x1 * n, self.y1 * n, 
                              self.x2 * n, self.y2 * n)

    def __rmul__(self, n):
        return self.__class__(self.x1 * n, self.y1 * n, 
                              self.x2 * n, self.y2 * n)

    def __getitem__(self, idx):
        return [(self.x1, self.y1), (self.x1, self.y2), 
                (self.x2, self.y2), (self.x2, self.y1)][idx]
    
    def __bool__(self):
        return True if (self.x2 - self.x1) * (self.y2 - self.y1) else False
    
    def __del__(self):
        print(f"Deleting {str(self)}")
        self.__class__.rectcnt -= 1

    def __iter__(self):
        return iter(((self.x1, self.y1), (self.x1, self.y2), 
                (self.x2, self.y2), (self.x2, self.y1)))        



for x, y in Rectangle(1, 2, 5, 6):
    print(x, y)


'''
d1 = Rectangle(1, 2, 3, 4)
print(d1)
d2 = Rectangle(5, 6, 7, 8)
print(d2)
d3 = Rectangle(1, 3, 8, 9)
print(d3)

for i in d1:
    print(i)
'''