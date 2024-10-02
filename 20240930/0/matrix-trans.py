str = list(eval(input()))
lst = [str]
while line := input():
    lst.append(list(eval(line)))

if all(len(i) == len(lst) for i in lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            lst[i][j], lst[j][i] = lst[j][i], lst[i][j]

for i in lst:
    print(i)