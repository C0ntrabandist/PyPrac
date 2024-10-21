from collections import defaultdict

line = input()

result = defaultdict(int)
for i in line.split():
    result[i] += 1

print(result)