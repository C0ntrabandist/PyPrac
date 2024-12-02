with open("text.txt", "rb") as file:
    data = file.read()
with open("text.txt", "wb") as file:
    file.write(data[len(data)//2+1:])
    file.write(data[:len(data)//2])