line = input()
vovels = set("aeiouy")
non_vovels = set("bcdfghjklmnpqrstvwxz")

count_vovel = {i for i in line if i in vovels}
count_non_vovel = {i for i in line if i in non_vovels}

print(len(count_vovel), len(count_non_vovel))
