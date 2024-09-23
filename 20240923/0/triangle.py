a, b, c = eval(input())

if a <= 0 or b <= 0 or c <= 0:
    print("Ne Treug")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Ne Treug")
else:
    print("Treug")
