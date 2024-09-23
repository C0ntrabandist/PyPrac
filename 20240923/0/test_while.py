ans = 0
ct = 1
while s := int(input()):
    if s == ct:
        ans = ans + 1
    ct += 1
print(ans)
