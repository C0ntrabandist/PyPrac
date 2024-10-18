from math import *

def scale(a, b, A, B, x):
    return (B - A) * (x - a) / (b - a) + A

W, H, A, B, formula = input().split()
W, H, A, B = int(W), int(H), float(A), float(B)
f = lambda x: eval(formula)
x_values = [scale(0, W - 1, A, B, i) for i in range(W)]
y_values = [f(x) for x in x_values]

y_min, y_max = min(y_values), max(y_values)
screen = [[' ' for _ in range(W)] for _ in range(H)]
p = round(scale(y_min, y_max, 0, H - 1, y_values[0]))

for i in range(1, W):
    y = round(scale(y_min, y_max, 0, H - 1, y_values[i]))
    if 0 <= y < H:
        screen[y][i] = '*'
        for j in range(min(y, p), max(y, p)):
            screen[j][i - 1] = '*'
    p = y

for row in screen[::-1]:
    print(''.join(row))

