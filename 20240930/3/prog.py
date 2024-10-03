
def mult(matrix1, matrix2):

  n = len(matrix1)
  res = [[0 for i in range(n)] for j in range(n)]
  
  for i in range(n):
    for j in range(n):
      res[i][j] = 0
      for k in range(n):
        res[i][j] = res[i][j] + matrix1[i][k] * matrix2[k][j]
  print()
  return res

def in_matrix(n, matrix):

  for _ in range(n):
    row = list(eval(input()))
    matrix.append(row)
  return matrix

mtx1 = []
mtx2 = []
res_m = []

str1 = list(eval(input()))
mtx1.append(str1)
n = len(str1)
mtx1 = in_matrix(n-1, mtx1)
mtx2 = in_matrix(n, mtx2)

'''
print('*----*')
print(f"Матрица 1: {mtx1}")
print('*----*')
print(f"Матрица 2: {mtx2}")
print('*----*')
#print(type(mtx1[0][0]))
#print(type(mtx1[0][0]))
#print('----')
'''
res_m = mult(mtx1, mtx2)


for m in res_m:
  print(*m, sep=",")
