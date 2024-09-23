match eval(input()):
    case 1:
        print("Odin")
    case 2:
        print("Dwa")
    case 3:
        print("Three")
    case val if val > 0:
        print(val, "Positive")
    case _:   
       print("unknown")
