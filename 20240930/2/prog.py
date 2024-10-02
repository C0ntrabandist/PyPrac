def sort(m):
 n = len(m)
 for i in range(n):
  for j in range(i + 1, n):
   key_i = (m[i] ** 2) % 100
   key_j = (m[j] ** 2) % 100
   if key_i > key_j:
    m[i], m[j] = m[j], m[i]

 return m

n = input().split(',')
n = [int(x) for x in n]

sorted = sort(n)

print(sorted)
