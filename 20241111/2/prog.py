class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = map(tuple, (a, b, c))

    def __abs__(self):
        x1, y1 = self.a
        x2, y2 = self.b
        x3, y3 = self.c
        area = 0.5 * abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1))
        return round(area, 3) or 0

    def __bool__(self):
        return abs(self) != 0

    def __lt__(self, other):
        return abs(self) < abs(other)

    def contains_point(self, p):
        x, y = p
        def sign(pa, pb):
            return (pa[0] - x)*(pb[1] - y) - (pb[0] - x)*(pa[1] - y)
        s1, s2, s3 = sign(self.a, self.b) >= 0, sign(self.b, self.c) >= 0, sign(self.c, self.a) >= 0
        return s1 == s2 == s3

    def __contains__(self, other):
        if isinstance(other, Triangle):
            larger, smaller = (self, other) if abs(self) >= abs(other) else (other, self)
            return abs(smaller) == 0 or other is self or all(self.contains_point(pt) for pt in [smaller.a, smaller.b, smaller.c])
        return False

    def __and__(self, other):
        if not self or not other:
            return False
        edges1 = [(self.a, self.b), (self.b, self.c), (self.c, self.a)]
        edges2 = [(other.a, other.b), (other.b, other.c), (other.c, other.a)]
        for (x1, y1), (x2, y2) in edges1:
            if x2 == x1:
                continue
            a1, b1 = (y2 - y1) / (x2 - x1), y1 - ((y2 - y1) / (x2 - x1)) * x1
            for (u1, v1), (u2, v2) in edges2:
                if u2 == u1:
                    continue
                a2, b2 = (v2 - v1) / (u2 - u1), v1 - ((v2 - v1) / (u2 - u1)) * u1
                if (((u1 * a1 + b1 - v1) > 0) != ((u2 * a1 + b1 - v2) > 0)) and \
                   (((x1 * a2 + b2 - y1) > 0) != ((x2 * a2 + b2 - y2) > 0)):
                    return True
        return False


    
import sys
exec(sys.stdin.read())