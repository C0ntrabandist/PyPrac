print(list(filter(None, [1, 32, 6, 0, 56, 32, 123, 6, 0, 0])))
print(list(filter(lambda x: x > 5, [1, 32, 6, 0, 56, 32, 123, 6, 0, 0])))
print(list(filter(lambda x: x < 5, [1, 32, 6, 0, 56, 32, 123, 6, 0, 0])))