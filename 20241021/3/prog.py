from collections import Counter

n = int(input())
c = Counter()
seps = "'-,.!?:\""

while (s := input().lower()):
        for sep in seps:
            s = s.replace(sep, ' ')
        words = s.split()
        c.update(w for w in words if len(w) == n)

if c:
    m = max(c.values())
    print(*sorted(w for w in c if c[w] == m))
