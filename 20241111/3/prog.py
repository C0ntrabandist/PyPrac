class Maze:
    def __init__(self, n):
        s = 2 * n + 1
        self.g = [['█'] * s for _ in range(s)]
        for i in range(n):
            for j in range(n):
                self.g[2 * i + 1][2 * j + 1] = '·'

    def __setitem__(self, key, val):
        y0, x_slice, x1 = key
        xs, y1 = x_slice.start, x_slice.stop
        if xs == x1:
            for j in range(2 * min(y0, y1) + 1, 2 * max(y0, y1) + 2):
                if (j + 2 * xs + 1) % 2:
                    self.g[2 * xs + 1][j] = val
        if y0 == y1:
            for i in range(2 * min(xs, x1) + 1, 2 * max(xs, x1) + 2):
                if (i + 2 * y0 + 1) % 2:
                    self.g[i][2 * y0 + 1] = val

    def __getitem__(self, key):
        y0, x_slice, x1 = key
        xs, ys = x_slice.start * 2 + 1, y0 * 2 + 1
        xe, ye = x1 * 2 + 1, x_slice.stop * 2 + 1
        stack, seen = [(xs, ys)], set()
        while stack:
            x, y = stack.pop()
            if (x, y) == (xe, ye):
                return True
            if (x, y) in seen:
                continue
            seen.add((x, y))
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < len(self.g) and 0 <= ny < len(self.g[0]) and
                        self.g[nx][ny] == '·' and (nx, ny) not in seen):
                        stack.append((nx, ny))
        return False

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.g)




import sys
exec(sys.stdin.read())