def is_dominated(x, y, a, b):
    return (x <= a and y <= b) and (x < a or y < b)

def Pareto(*pairs):
    pareto_front = []
    for i in range(len(pairs)):
        iso = False
        for j in range(len(pairs)):
            if i != j and is_dominated(*pairs[i], *pairs[j]):
                iso = True
                break
        if not iso:
            pareto_front.append(pairs[i])
    return tuple(pareto_front)

data = eval(input())
print(Pareto(*data))
