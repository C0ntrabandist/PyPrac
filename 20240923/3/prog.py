in_data = int(input())
rows = 0
while rows < 3:
    col = 0
    while col < 3:
      num1 = in_data + rows
      num2 = in_data + col
      product = num1 * num2
      print(f"{num1} * {num2} =", end=" ")
      sum_of_digits = 0
      tmp = product
      while tmp > 0:
        sum_of_digits += tmp % 10
        tmp //= 10
      if sum_of_digits == 6:
        print(":=)", end=" ")
      else:
        print(product, end=" ")
      col += 1
    print()
    rows += 1
