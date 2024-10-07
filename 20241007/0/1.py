def average(*args):
    return sum(args) / len(args) if len(args) != 0 else "Error input!"

print(average(1, 2, 3, 4, 5))
print(average())
