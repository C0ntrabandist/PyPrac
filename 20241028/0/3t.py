def biased(init):
     print("QQ")
     bias = yield init
     while bias:
         init += bias*2+1
         bias = yield init

g = biased(5)
res = next(g)
print(res)

res = g.send(5)
print(res)

res = g.send(123)
print(res)

res = g.send(100500)
print(res)