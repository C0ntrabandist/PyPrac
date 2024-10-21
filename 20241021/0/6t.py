from collections import Counter
import timeit
from collections import defaultdict
#line = input().split()
line = input().split()

def word_count():
    result = defaultdict(int)
    for i in line:
        result[i] += 1

    return result

print(timeit.Timer(word_count).autorange())
print(timeit.Timer("len(Counter(line))", globals=globals()).autorange())