with open("text.txt") as f:
    data = f.read()
t=data[len(data)//3+1:].find("\n")
print(data[:len(data)//3+t+1])