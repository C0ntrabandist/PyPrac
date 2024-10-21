import timeit
import string


#line = input()
line = set(input("In data:"))
vovels = set("aeiouy")
non_vovels = set(string.ascii_lowercase) - vovels

'''
def count_letters():
    count_vovel = {i for i in line if i in vovels}
    count_non_vovel = {i for i in line if i in non_vovels}
    return len(count_vovel), len(count_non_vovel)
'''

def count_letters():
    return (len(line & vovels), len(line & non_vovels))

print(timeit.Timer(count_letters).autorange())
