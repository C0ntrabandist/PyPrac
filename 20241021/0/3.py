import timeit

line = input()
vovels = set("aeiouy")
non_vovels = set("bcdfghjklmnpqrstvwxz")

def count_letters():
    count_vovel = {i for i in line if i in vovels}
    count_non_vovel = {i for i in line if i in non_vovels}
    return len(count_vovel), len(count_non_vovel)

print(timeit.Timer(count_letters).autorange())
