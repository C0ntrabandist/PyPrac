match eval(input()):
    case 1:
        print("Odin")
    case 2:
        print("Dwa")
    case 3:
        print("Three")
    case even if even % 2 == 0:
        print(even, "Even")
    case odd if odd % 2 != 0:
        print(odd, "Odd")
    case _:
       print("unknown")
