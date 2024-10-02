'''
def mult(matrix1, matrix2):

  n = len(matrix1)
  res = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        res[i][j] += matrix1[i][k] * matrix2[k][j]
  return res
'''

def in_matrix(n):

  matrix = []
  for _ in range(n):
    row = list(eval(input()))
    matrix.append(row)
  return matrix

mtx1 = []
mtx2 = []
res_m = []

str1 = list(eval(input()))
n = len(str1)
mtx1.append(str1)
mtx1.append(in_matrix(n-1)) 
mtx2 = in_matrix(n)

for i in range(n):
    for j in range(n):
        sum = 0
        for k in range(n):
            sum += mtx1[i][k] * mtx2[k][j]
        print(sum, end='')
        if j != n - 1: print('', end=',')
    print()
'''
for m in res_m:
  print(*m, sep=",")
'''