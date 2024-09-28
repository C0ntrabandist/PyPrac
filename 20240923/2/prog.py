limit = 21  

total_sum = 0
last_num = None
while (last_num := int(input())) > 0:
  total_sum += last_num
  if total_sum > limit:
    print(total_sum)
    break
else:
    print(last_num)