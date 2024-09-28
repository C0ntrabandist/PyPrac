num = int(input())

output = "A"

if num % 25 == 0:
    if num % 2 == 0:
        output += " + B -"
    else:
        output += " - B +"
else:
    output += " - B -"

if num % 8 == 0:
    output += " C +"
else:
    output += " C -"

print(output)
