from fractions import Fraction

s, w, *tail = map(Fraction, input().split(", "))
na = int(tail[0])
nb = int(tail[na + 2])
pa = sum(tail[i] * s**(na - i + 1) for i in range(1, na + 2))
pb = sum(tail[i] * s**(nb - i + 1) for i in range(na + 3, na + 3 + nb + 1)) * w

print(pa == pb)
